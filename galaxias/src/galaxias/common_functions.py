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