import pandas as pd

def read_dwc_terms():
    '''Reads in accepted DwC terms from the given link to a csv'''

    dwc_terms = pd.read_csv("https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/terms-versions/terms-versions.csv")
    dwc_terms_recommended = dwc_terms[dwc_terms["version_status"] == "recommended"].reset_index(drop=True)
    list_terms_recommended = list(dwc_terms_recommended["term_localName"])
    return list_terms_recommended

def get_dwc_values():

    n=1

def get_dwc_noncompliant_terms(dataframe = None):
    
    # get current terms in 
    list_terms = list(dataframe.columns)

    # get all available terms
    available_terms = read_dwc_terms()

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