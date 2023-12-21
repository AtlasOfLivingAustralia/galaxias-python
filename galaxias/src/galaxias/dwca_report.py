from .common_dictionaries import REPORT_TERMS
from .galaxias_config import readConfig

def dwca_report(report = None,
                verbose = False,
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
                       'all_required_columns_present','missing_columns','taxonomy_report']
    members_reports = ['records_with_taxonomy_count','records_with_temporal_count',
                       'coordinates_report','column_counts']

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

    #if report_dict['record_error_count'] > 0:
    if report_dict['How many records have full taxa?'] < report_dict['Number of Records']:
        if report_dict['Errors'] is not None:
            report_dict['Errors'].append("Some records don't have the full taxonomic classification.  Use X to fix this")
        else:
            report_dict['Errors'] = ["Some records don't have the full taxonomic classification.  Use X to fix this"]
        report_dict['Number of Errors in Records'] += report_dict['Number of Records'] - report_dict['How many records have full taxa?']

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
            if entry == "Spatial validity of coordinates":
                print(entry + ":")
                print("\tData has coordinate fields?: {}".format(report_dict[entry].has_coordinates_fields))
                print("\tInvalid latitude count: {}".format(report_dict[entry].invalid_decimal_latitude_count))
                print("\tInvalid longitude count: {}".format(report_dict[entry].invalid_decimal_longitude_count))
            elif entry == "Number of entries in each column":
                print(entry + ":")
                for column in report_dict[entry]:
                    print("\t{}: {}".format(column,report_dict[entry][column]))
            elif entry == "Missing Columns":
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
                    print("\tUnrecognised taxa: {}".format(report_dict[entry].unrecognised_taxa))
                    if len(report_dict[entry].suggested_names) > 0:
                        for key in report_dict[entry].suggested_names:
                            print("\n{}\n{}\n".format(key,report_dict[entry].suggested_names[key]))
                    else:
                        print("\tInvalid taxon present: {}".format(report_dict[entry].suggested_names))
                else:
                    print("Could not do a taxonomic classification because scientificName is likely missing from your columns.")
            else:
                print("{}: {}".format(entry,report_dict[entry]))
        report_file.write("{}: {}\n".format(entry,report_dict[entry]))
    report_file.close()         