import pandas as pd

def read_dwc_terms_list():
    '''Reads in accepted DwC terms from the given link to a csv'''

    # dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/master/vocabulary/term_versions.csv")
    dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms-versions/terms-versions.csv")
    dwc_terms_recommended = dwc_terms[dwc_terms["version_status"] == "recommended"].reset_index(drop=True)
    list_terms_recommended = list(dwc_terms_recommended["term_localName"]) + ['identifier'] # temporary until we fix stuff with multimedia
    return list_terms_recommended

def read_dwc_terms_links():
    '''Reads in accepted DwC terms from the given link to a csv'''

    # dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/dwc/master/vocabulary/term_versions.csv")
    dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms-versions/terms-versions.csv") # version_status
    dwc_terms_rec = dwc_terms[dwc_terms["version_status"] == "recommended"].reset_index(drop=True)
    dwc_terms_info = pd.DataFrame({'name': list(dwc_terms_rec['term_localName']), 'link': ["".join([row['version_isDefinedBy'].replace('version/',""),
                                                row['term_localName']]) for i,row in dwc_terms_rec.iterrows()]})
    dwc_terms_info = pd.concat([dwc_terms_info,pd.DataFrame({'name': 'identifier', 'link': 'http://rs.tdwg.org/dwc/terms/version/identifier'},index=[0])]).reset_index(drop=True) # temporary until we fix stuff with multimedia
    return dwc_terms_info

def get_dwc_values():

    n=1

def get_dwc_noncompliant_terms(dataframe = None):
    
    # get current terms in 
    list_terms = list(dataframe.columns)

    # get all available terms
    available_terms = read_dwc_terms_list()

    # look for non-compliant terms
    if any(map(lambda v: v not in available_terms, list_terms)):
    
        # check for missing fields
        check_missing_fields = set(available_terms).issuperset(list_terms)
        
        # check for any missing required fields
        if (not check_missing_fields) or (type(check_missing_fields) is not bool and len(check_missing_fields) > 0):
            
            # get any incorrect terms
            incorrect_dwc_terms = set(dataframe.columns).difference(set(available_terms))
            
            # return list
            if len(incorrect_dwc_terms) == 0:
                return []
            else:
                return list(incorrect_dwc_terms)
    
    else:

        return []