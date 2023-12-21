import requests
import pandas as pd
import re

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