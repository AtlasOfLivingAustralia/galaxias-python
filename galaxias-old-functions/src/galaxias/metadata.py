import os
import pandas as pd

def read_dwc_terms():
    '''Reads in accepted DwC terms from the given csv file'''

    # read file and generate pandas dataframe
    dwc_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'darwin_core-terms.csv')
    dublicore_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dublincore-terms.csv')
    dwc = pd.read_csv(dwc_file)
    dbc = pd.read_csv(dublicore_file)
    dwc_terms = pd.concat([dwc,dbc],ignore_index=True)
    return dwc_terms

def update_dwc_terms():
    '''Checks for new DarwinCore terms and updates them accordingly'''

    n=1

def create_metadata_file(path="."):
    '''Create a markdown file for the user to edit'''

    os.system("cp {} {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'metadata_template.md'),path))

def update_md():
    '''Function mainly for the website - edit md directly'''

    n=1

def write_eml_xml():
    '''Writes data into properly formatted eml.xml'''

    n=1

def write_meta_xml(dataframe=None):
    '''Writes data into properly formatted meta.xml'''

    n=1