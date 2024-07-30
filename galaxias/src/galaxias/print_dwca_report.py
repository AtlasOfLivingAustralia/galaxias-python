from tabulate import tabulate
import pandas as pd

def print_dwca_report(dataframe=None,
                      matched_dwc_terms=None,
                      unmatched_dwc_terms=None,
                      required_terms=None):

    print("\n── Darwin Core terms ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("\n── All DwC terms ──")
    # change to include events, multimedia and emof
    print("\nMatched {} of {} column names to DwC terms:\n".format(len(matched_dwc_terms),len(dataframe.columns)))
    print("{} Matched: {}".format(u'\u2713',', '.join(matched_dwc_terms)))
    print("{} Unmatched: {}".format(u'\u2717',', '.join(unmatched_dwc_terms)))
    print("\n── Minimum required DwC terms ──\n")
    terms = pd.DataFrame(required_terms)
    print(tabulate(terms, showindex=False, headers=terms.columns))
    print("\n── Suggested workflow ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    if list(required_terms["Missing term(s)"]) == ['-','-','-','-','-']:
        print("\nCongratulations! Your data is now Darwin Core compliant. You can write the metadata using the command")
        print("\nmy_dwca.write_eml_xml()")
        print("my_dwca.write_meta_xml()")
        print("\nand then you can make your Darwin Core Archive by running")
        print("\nmy_dwca.create_dwca()")
    else:
        print("To make your data Darwin Core compliant, use the following workflow:\n")
        if required_terms["Matched term(s)"][0] == '-' or required_terms["Matched term(s)"][1] == '-':
            print("df.use_occurrences()")
        if required_terms["Matched term(s)"][2] == '-':
            print("df.use_scientific_name()")
        if required_terms["Missing term(s)"][3] != '-':
            print("df.use_coordinates()")
        if required_terms["Matched term(s)"][4] == '-':
            print("df.use_datetime()")    
        print("\nAdditional functions: use_locality()")