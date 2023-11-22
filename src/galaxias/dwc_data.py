import os
import requests
import pandas as pd
import numpy as np
from .metadata import read_dwc_terms
from .galaxias_config import readConfig
from operator import itemgetter
import difflib
import json
import copy
from .common_dictionaries import REQUIRED_DWCA_TERMS,NAME_MATCHING_TERMS,ID_REQUIRED_DWCA_TERMS,GEO_REQUIRED_DWCA_TERMS

# testing
import sys

'''
from bs4 import BeautifulSoup
from pandas.testing import assert_frame_equal

def webscrape_dwc():

    # websites to get terms from
    dwc_terms_website = "http://rs.tdwg.org/dwc/terms.htm"
    dublincore_terms_website = "http://rs.tdwg.org/dwc/dcterms.htm"
    
    # look for JSON, XML instead of web scraping (TWDG RDF?)
    # table with names + URLs (TDWG?)

    # DarwinCore headers
    dwc_response = requests.get(dwc_terms_website)
    soup_dwc = BeautifulSoup(dwc_response.text, 'html.parser')

    # DublinCore headers
    dublin_response = requests.get(dublincore_terms_website)
    soup_dublin = BeautifulSoup(dublin_response.text, 'html.parser')

    # test this
    dwc_table_titles = soup_dwc.find_all("h2")
    for i,title in enumerate(dwc_table_titles):
        if title.text.strip() == "4 Terms that are members of this list":
            index_dwc=i

    dublin_table_titles = soup_dublin.find_all("h2")
    for i,title in enumerate(dublin_table_titles):
        if title.text.strip() == "4 Terms that are members of this list":
            index_dublin=i

    # get individual tables
    dwc_table_to_parse = soup_dwc.find_all('table')[index_dwc:]
    dublin_table_to_parse = soup_dublin.find_all('table')[index_dublin:]

    # put all terms in a table
    table_of_terms_to_parse = dwc_table_to_parse + dublin_table_to_parse
    
    # make dictionary for all terms
    dwc_terms = {"Term Name": ["" for n in range(len(table_of_terms_to_parse))],
                 "Label": ["" for n in range(len(table_of_terms_to_parse))],
                 "Term IRI": ["" for n in range(len(table_of_terms_to_parse))],
                 "Term version IRI": ["" for n in range(len(table_of_terms_to_parse))],
                 "Modified": ["" for n in range(len(table_of_terms_to_parse))],
                 "Definition": ["" for n in range(len(table_of_terms_to_parse))],
                 "Type": ["" for n in range(len(table_of_terms_to_parse))],
                 "Used": [True for n in range(len(table_of_terms_to_parse))],
                 "Note": ["" for n in range(len(table_of_terms_to_parse))],
                 "Replacement": ["" for n in range(len(table_of_terms_to_parse))]}

    for i,row in enumerate(table_of_terms_to_parse):  

        # Find all data for each column
        columns = row.find_all('td')
        
        # if columns aren't empty, get data within columns
        if(columns != []):
            
            for j,entry in enumerate(columns):

                # check for column names and assign appropriate values
                if any(term.lower() in entry.text.lower() for term in dwc_terms.keys()) and "http" not in entry.text:
                    index = [name for name in dwc_terms.keys() if name.lower() in entry.text.lower()][0]
                    if "note" in entry.text.lower():
                        if "this term is no longer" in columns[j+1].text.strip().lower():
                            dwc_terms["Used"][i] = False
                    dwc_terms[index][i] = columns[j+1].text.strip()

                elif "replaces" in entry.text.lower():
                    dwc_terms["Replacement"][i] = columns[j+1].text.strip()

                else:
                    pass

    # return dataframe with all data
    return pd.DataFrame.from_dict(dwc_terms)

def check_for_update_dwc():

    current_dwc_terms = read_dwc_terms()
    new_dwc_terms = webscrape_dwc()
    print(assert_frame_equal(current_dwc_terms,new_dwc_terms))
    if not current_dwc_terms.equals(new_dwc_terms):
       new_dwc_terms.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dwc_terms.csv'),index=False)
    else:
        print("just for testing")    
'''

def check_dwca_column_names(dataframe=None,
                            return_invalid_values=False):
    '''Check all Darwin Core column names and provides alternatives to ones that are incorrect/invalid'''

    # configs
    configs = readConfig()

    # get atlas
    atlas = configs["galaxiasSettings"]["atlas"]

    # get all variables for checking
    dwc_terms_df = read_dwc_terms()
    dwc_terms = list(dwc_terms_df['term'])
    #print(dwc_terms)
    column_names = list(dataframe.columns)
    bool_list = list(map(lambda v: v in dwc_terms, column_names))
    missing_requirements = []
    check_required_dwca_terms = list(map(lambda v: v in column_names, REQUIRED_DWCA_TERMS[atlas]))
    for check,term in zip(check_required_dwca_terms,REQUIRED_DWCA_TERMS[atlas]):
        if not check:
            missing_requirements.append(term)
    check_id_required_dwca_terms = list(map(lambda v: v in column_names,ID_REQUIRED_DWCA_TERMS[atlas]))
    if not any(check_id_required_dwca_terms):
        missing_requirements.append(ID_REQUIRED_DWCA_TERMS[atlas][0])
    check_geo_required_dwca_terms = list(map(lambda v: v in column_names,GEO_REQUIRED_DWCA_TERMS[atlas]))
    missing_geo_requirements = []
    for check,term in zip(check_geo_required_dwca_terms,GEO_REQUIRED_DWCA_TERMS[atlas]):
        if not check:
            missing_geo_requirements.append(term)
    invalid_dwca_terms = {}

    # check if terms are valid, and if not, provide suggestions
    if not all(bool_list):
        for name,check in zip(column_names,bool_list):
            if check is False:
                if "species" in name.lower():
                    print("here")
                    invalid_dwca_terms[name] = difflib.get_close_matches("scientific",dwc_terms)
                elif "date" in name.lower():
                    invalid_dwca_terms[name] = difflib.get_close_matches("dateIde",dwc_terms)
                    invalid_dwca_terms[name] += (difflib.get_close_matches(name,dwc_terms))
                else:
                    invalid_dwca_terms[name] = difflib.get_close_matches(name,dwc_terms)
        if return_invalid_values:
            return invalid_dwca_terms,missing_requirements,missing_geo_requirements
        else:
            print("The following are all invalid DarwinCore terms, and the closest suggestions follow:")
            for key in invalid_dwca_terms:
                print("{}: {}".format(key,invalid_dwca_terms[key]))
            print("\nYou are missing these required fields.  These may not exist in the data, or need their title changed.\n")
            for key in missing_requirements:
                print(key)
            print("\nYou might be missing geospatial requirements:\n")
            for key in missing_geo_requirements:
                print(key)
            return
    return True
    
def check_for_duplicates(dataframe=None):
    '''Make sure there are no duplicate column names'''
    
    if dataframe is not None:
        columns = list(dataframe.columns)
        set_columns = set(columns)
        if len(set_columns) < len(columns):
            return False
        return True
    else:
        raise ValueError("Please provide a data frame to this function.")

def rename_dwc_columns(dataframe=None,
                       names=None):
    '''Function for automatically renaming dwc columns'''

    if names is not None and dataframe is not None:

        if check_for_duplicates(dataframe):

            # add another column to specify rank if species is in column name
            if any("species" in key for key in dataframe.keys()):
                index = [i for i,name in enumerate(dataframe.columns) if "species" in name.lower()][0]
                dataframe.insert(loc=index,column="rank",value="species") 
            
            # rename columns to comply with dwc standards
            return dataframe.rename(names,axis=1)
        
        else:

            raise ValueError("You have got duplicate column headings.  Remove or rename columns and run this function again.")
    
    else:

        raise ValueError("Please provide a dataframe, as well as a dictionary of current and desired names.")

def check_dwca_column_formatting(dataframe=None):

    column_names = list(dataframe.columns)
    print(column_names)

def check_species_names(dataframe=None,
                        num_matches=5,
                        include_synonyms=True,
                        return_matches = False):
    """
    Checks species names against the ALA repository.  Provides alternatives for ones that are homonyms or are not in the database.

    Parameters
    ----------
        dataframe : `pandas` dataframe
            Dataframe containing species name you want to turn into a Darwin Core Archive. 
        num_matches : int
            Number of matching names you want to be provided in case there is a mismatched name.  Default to 5. 
        include_synonyms : logical
            Includes possible synonyms for your species. Default to `True`.
        return_matches : logical
            Option whether to return a dictionary object containing species names and alternatives.  Default to `False`.   

    Returns
    -------
        Either `True`, `False` or a dictionary object containing species names and alternatives.

    Examples
    --------

    Something here.

    # .. prompt:: python

    #     import galaxias
    #     X

    # .. program-output:: python -c "import galaxias;"
    """

    # configs
    configs = readConfig()

    # get atlas
    atlas = configs["galaxiasSettings"]["atlas"]

    # check for scientificName, as users should check that they have the correct column names
    if "scientificName" not in list(dataframe.columns):
        raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")
    
    # make a list of all scientific names in the dataframe
    scientific_names_list = list(set(dataframe["scientificName"]))
    
    # send list of scientific names to ALA to check their validity
    payload = [{"scientificName": name} for name in scientific_names_list]
    response = requests.request("POST","https://api.ala.org.au/namematching/api/searchAllByClassification",data=json.dumps(payload))
    response_json = response.json()
    verification_list = {"scientificName": scientific_names_list, "issues": [None for i in range(len(scientific_names_list))]}
    
    # loop over list of names and ensure we have gotten all the issues - might need to do single name search
    # to ensure we get everything
    for i,item in enumerate(scientific_names_list):
        item_index = next((index for (index, d) in enumerate(response_json) if "scientificName" in d and d["scientificName"] == item), None)
        if item_index is not None:
            verification_list["issues"][i] = response_json[item_index]["issues"]
        else:
            response_single = requests.get("https://api.ala.org.au/namematching/api/search?q={}".format("%20".join(item.split(" "))))
            response_json_single = response_single.json()
            if response_json_single['success']:
                verification_list["issues"][i] = response_json_single["issues"]
            else:
                verification_list["issues"][i] = response_json_single["issues"]

    # check for homonyms - if there are any, then print them out to the user so the user can disambiguate the names
    df_verification = pd.DataFrame(verification_list)
    if any(df_verification.loc[df_verification['issues'].astype(str).str.contains("homonym",case=False,na=False)]):
        print("You have one or more invalid taxa in your data.  Invalid taxa are:\n")
        invalid_taxon = df_verification.loc[df_verification['issues'].astype(str).str.contains("homonym",case=False,na=False)]
        print(invalid_taxon)
        print("\nSuggested names are below:\n")
        matches = {x: None for x in invalid_taxon['scientificName']}
        for name in invalid_taxon['scientificName']:
            print(name)
            print()
            response = requests.get("https://api.ala.org.au/namematching/api/autocomplete?q={}&max={}&includeSynonyms={}".format("%20".join(name.split(" ")),num_matches,str(include_synonyms).lower()))
            data = {x: [] for x in NAME_MATCHING_TERMS[atlas]}
            response_json = response.json()
            list_names = [x["name"] for x in response_json]
            for item in list_names:
                response_single = requests.get("https://api.ala.org.au/namematching/api/search?q={}".format("%20".join(item.split(" "))))
                response_json_single = response_single.json()
                names_df = pd.DataFrame()
                if response_json_single['success']:
                    for item in NAME_MATCHING_TERMS[atlas]:
                        if item in response_json_single:
                            data[item].append(response_json_single[item])
                        else:
                            data[item].append(None)
            names_df = pd.DataFrame(data)
            if return_matches:
                matches[name] = names_df
            print(names_df)
        if return_matches:
            return(matches)
        return False
    return True

def check_spatial_validity(dataframe=None):

    columns_list = list(dataframe.columns)

    if "decimalLatitude" not in columns_list or "decimalLongitude" not in columns_list:
        raise ValueError("Before checking the spatial validity of your data, ensure all your column names comply to DwCA standard.  decimalLatitude and decimalLongitude are the column names you are looking for.")
    

    n=1