import os
import requests
from .dwc_data import *

def create_dwca(datafile="data.csv",
                eml="eml.xml",
                meta="meta.xml",
                filename="dwca.zip"):

    if not check_for_duplicates():
        raise ValueError("Some of your columns are duplicates.  Please remove them before starting again.")
    if not check_dwca_column_names(dataframe=datafile):
        raise ValueError("Some of your DwCA columns are not named correctly.  Please check again.")
    if not check_dwca_column_formatting():
        raise ValueError("Some of your columns are not formatted correctly.")
    
    os.system("zip {} {} {} {}".format(filename,datafile,eml,meta))

def post_dwca_ala(dwca=None):
    '''Function for posting completed DwCA to the ALA'''

    response = requests.request("POST","",data={})