import os
import pandas as pd

def read_dwc_terms():
    '''Reads in accepted DwC terms from the given csv file'''

    # read file and generate pandas dataframe
    dwc_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'darwin_core-terms.csv')
    dublin_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dublincore-terms.csv')
    print(pd.read_csv(dwc_file))
    print(pd.read_csv(dublin_file))
    dwc_terms = pd.read_csv(dwc_file)
    dublin_terms = pd.read_csv(dublin_file)
    print()
    print(pd.concat([dwc_terms,dublin_terms]))
    #return pd.read_csv(dwc_file)

def update_dwc_terms():
    '''Checks for new DarwinCore terms and updates them accordingly'''

    n=1

def create_metadata_file(path="."):
    '''Create a markdown file for the user to edit'''

    os.system("cp {} {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'metadata_template.md'),path))

def update_eml_xml():
    '''Function mainly for the website - edit md directly'''

    n=1

def write_eml_xml():
    '''Writes data into properly formatted eml.xml'''

    n=1

def write_meta_xml(dataframe=None):
    '''Writes data into properly formatted meta.xml'''

    n=1