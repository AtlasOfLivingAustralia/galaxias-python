import os
import requests
import pandas as pd
from .metadata import read_dwc_terms
import difflib

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

def check_dwca_column_names(dataframe=None,return_invalid_values=False):
    '''Check all Darwin Core column names and provides alternatives to ones that are incorrect/invalid'''

    # get all variables for checking
    dwc_terms = read_dwc_terms()
    column_names = list(dataframe.columns)
    bool_list = list(map(lambda v: v in dwc_terms, column_names))
    invalid_dwca_terms = {}

    # check if terms are valid, and if not, provide suggestions
    if not all(bool_list):
        for name,check in zip(column_names,bool_list):
            if check is False:
                if "species" in name.lower():
                    invalid_dwca_terms[name] = difflib.get_close_matches("scientific",dwc_terms)
                elif "date" in name.lower():
                    invalid_dwca_terms[name] = difflib.get_close_matches("dateIde",dwc_terms)
                    invalid_dwca_terms[name] += (difflib.get_close_matches(name,dwc_terms))
                else:
                    invalid_dwca_terms[name] = difflib.get_close_matches(name,dwc_terms)
        if return_invalid_values:
            return invalid_dwca_terms
        else:
            print("The following are all invalid DarwinCore terms, and the closest suggestions follow:")
            for key in invalid_dwca_terms:
                print("{}: {}".format(key,invalid_dwca_terms[key]))
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
    '''Function to do a basic check on whether or not the column has the correct formatting associated with its title'''

    column_names = list(dataframe.columns)
    print(column_names)