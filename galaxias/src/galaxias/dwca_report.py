from .common_dictionaries import REPORT_TERMS
from .galaxias_config import readConfig
import pandas as pd

def dwca_report(report = None,
                verbose = True, #False
                print_to_screen = True):

    # check for report
    if report is None:
        raise ValueError()
    
    # get atlas
    configs = readConfig()
    atlas = configs["galaxiasSettings"]["atlas"]

    # get all attributes of a report
    attributes_dict = REPORT_TERMS[atlas]
    
    # ideally make this not hard-coded but not sure how...
    ordered_members = ['record_type','record_count','record_error_count','errors','warnings',
                       'all_required_columns_present','missing_columns','taxonomy_report',
                       'datetime_report','incorrect_dwc_terms']
    members_reports = ['records_with_temporal_count','coordinates_report','column_counts',
                       ]

    # make report more human readable and check for passes
    report_dict_raw = report.__dict__
    report_dict = {"Pass/Fail": "Fail"}
    for om in ordered_members:
        if om == 'errors' or om == 'warnings':
            if not report_dict_raw[om]:
                report_dict[attributes_dict[om]] = None
            else:
                report_dict[attributes_dict[om]] = report_dict_raw[om]
        elif om == 'all_required_columns_present' or om == 'missing_columns':
            report_dict[attributes_dict[om]] = report_dict_raw[om]
        else:
            report_dict[attributes_dict[om]] = report_dict_raw[om]

    # check if user wants extras report
    if verbose:
        # add extras
        for mr in members_reports:
            report_dict[attributes_dict[mr]] = report_dict_raw[mr]

    ### TODO: FIX THIS
    #if report_dict['record_error_count'] > 0:
    # if report_dict['records_with_taxonomy_count'] < report_dict['record_count']:
    #     if report_dict['Errors'] is not None:
    #         report_dict['Errors'].append("Some records don't have the full taxonomic classification.  Use X to fix this")
    #     else:
    #         report_dict['Errors'] = ["Some records don't have the full taxonomic classification.  Use X to fix this"]
    #     report_dict['record_error_count'] += report_dict['record_count'] - report_dict['records_with_taxonomy_count']

    if report_dict["taxonomy_report"] is not None:
        if report_dict["taxonomy_report"].has_invalid_taxa:
            if report_dict['Errors'] is not None:
                report_dict['Errors'].append("There are some invalid taxa according to the backbone you are comparing against.")
            else:
                report_dict['Errors'] = ["There are some invalid taxa according to the backbone you are comparing against."]      
    else:
        report_dict['Errors'] = ["A taxonomy report could not be generated, likely because the column 'scientificName' is not in your column names."]      

    if not report_dict["all_required_columns_present"]:
        if report_dict['Errors'] is not None:
            report_dict['Errors'].append("You are missing required columns in your data.")
        else:
            report_dict['Errors'] = ["You are missing required columns in your data."]      

    if report_dict['datetime_report'] is not None:
        if report_dict['datetime_report'].has_invalid_datetime:
            if report_dict['Errors'] is not None:
                report_dict['Errors'].append("Your datetime format is not in YYYY-MM-DD or iso format.")
            else:
                report_dict['Errors'] = ["Your datetime format is not in YYYY-MM-DD or iso format."]      

    if report_dict['incorrect_dwc_terms'] is not None:
        if report_dict['Errors'] is not None:
            report_dict['Errors'].append("Some of your columns do not match the current Darwin Core Standard.")
        else:
            report_dict['Errors'] = ["Some of your columns do not match the current Darwin Core Standard."]      


    # check pass/fail based on errors and warnings
    if report_dict[attributes_dict['errors']] is None:
        report_dict["Pass/Fail"] = "Pass"

    # write report to file
    if verbose:
        report_file = open("./report_verbose.md","w")
    else:
        report_file = open("./report_basic.md","w")
    for entry in report_dict:
        if print_to_screen:
            if entry == "coordinates_report":
                print(entry + ":")
                print("\tData has coordinate fields?: {}".format(report_dict[entry].has_coordinates_fields))
                print("\tInvalid latitude count: {}".format(report_dict[entry].invalid_decimal_latitude_count))
                print("\tInvalid longitude count: {}".format(report_dict[entry].invalid_decimal_longitude_count))
            elif entry == "Number of entries in each column":
                print(entry + ":")
                for column in report_dict[entry]:
                    print("\t{}: {}".format(column,report_dict[entry][column]))
            elif entry == "missing_columns":
                if len(report_dict[entry]) > 0:
                    print("{}:".format(entry))
                    for v in report_dict[entry]:
                        print("\t{}".format(v))
                else:
                    print("{}: None".format(entry))
            elif entry == "taxonomy_report":
                if report_dict[entry] is not None:
                    print("Taxonomic validity:")
                    print("\tInvalid taxon present: {}".format(report_dict[entry].has_invalid_taxa))
                    print("\tValid Taxon count: {}".format(report_dict[entry].valid_taxon_count))
                    if report_dict[entry].has_invalid_taxa:
                        print("\tUnrecognised taxa:\n")
                        print(pd.DataFrame(report_dict[entry].unrecognised_taxa))
                        print()
                else:
                    print("Taxonomic validity:")
                    print("\tCould not do a taxonomic classification because 'scientificName' is likely missing from your columns.")
            elif entry == "Errors":
                if report_dict[entry] is not None:
                    print("Errors: ")
                    for e in report_dict[entry]:
                        print("\t{}".format(e))
                else:
                    print("Errors: None")
            elif entry == "column_counts":
                print("Column counts:")
                for e in report_dict[entry]:
                    print("\t{}: {}".format(e,report_dict[entry][e]))
            elif entry == "datetime_report":
                print("Datetime Report:")
                print("\tHas invalid datetime: {}".format(report_dict[entry].has_invalid_datetime))
                print("\tNumber of invalid datetimes: {}".format(report_dict[entry].num_invalid_datetime))
            elif entry == "incorrect_dwc_terms":
                print("Incorrect Darwin Core Terms:")
                for e in report_dict[entry]:
                    print("\t{}".format(e))
            else:
                print("{}: {}".format(entry,report_dict[entry]))
        report_file.write("{}: {}\n".format(entry,report_dict[entry]))
    report_file.close()         