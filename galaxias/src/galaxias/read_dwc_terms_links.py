import pandas as pd

def read_dwc_terms_links():
    '''Reads in accepted DwC terms from the given link to a csv'''

    # dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/master/vocabulary/term_versions.csv")
    dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms-versions/terms-versions.csv") # version_status
    dwc_terms_rec = dwc_terms[dwc_terms["version_status"] == "recommended"].reset_index(drop=True)
    dwc_terms_info = pd.DataFrame({'name': list(dwc_terms_rec['term_localName']), 'link': ["".join([row['version_isDefinedBy'].replace('version/',""),
                                                row['term_localName']]) for i,row in dwc_terms_rec.iterrows()]})
    dwc_terms_info = pd.concat([dwc_terms_info,pd.DataFrame({'name': 'identifier', 'link': 'http://rs.tdwg.org/dwc/terms/version/identifier'},index=[0])]).reset_index(drop=True) # temporary until we fix stuff with multimedia
    return dwc_terms_info