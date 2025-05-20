import pandas as pd

def read_dwc_terms_list():
    '''Reads in accepted DwC terms from the given link to a csv'''

    # dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/master/vocabulary/term_versions.csv")
    dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms-versions/terms-versions.csv")
    dwc_terms_recommended = dwc_terms[dwc_terms["version_status"] == "recommended"].reset_index(drop=True)
    list_terms_recommended = list(dwc_terms_recommended["term_localName"]) + ['identifier'] # temporary until we fix stuff with multimedia
    return list_terms_recommended