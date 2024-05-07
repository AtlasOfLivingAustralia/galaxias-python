from .common_dictionaries import REPORT_TERMS
from .galaxias_config import readConfig
import pandas as pd

def dwca_report(occurrence_report = None,
                events_report = None,
                multimedia_report = None,
                emof_report = None,
                verbose = True, #False
                print_to_screen = True):

    # check for report
    if occurrence_report is None and events_report is None:
        raise ValueError("Need occurrences or events")
    
    if occurrence_report is None:
        raise ValueError("Need occurrences")
    
    # get atlas
    # configs = readConfig()
    # atlas = configs["galaxiasSettings"]["atlas"]
    atlas = "Australia"
    
    # check for event or occurrence dataset; set it 
    report_dict = {"Pass/Fail": "Fail"}
    if events_report is not None:
        report_dict["Data Type"] = "Event"
        report_dict["Events Report"] = events_report.__dict__
        report_dict["Occurrences"] = occurrence_report.__dict__
    else:
        report_dict["Data Type"] = "Occurrence"
        report_dict["Events Report"] = None
        report_dict["Occurrences"] = occurrence_report.__dict__

    # add multimedia extension
    if multimedia_report is not None:
        report_dict["Multimedia"] = multimedia_report.__dict__
    else:
        report_dict["Multimedia"] = None

    # add emof extension
    if emof_report is not None:
        report_dict["Extended Measurement Or Fact"] = emof_report.__dict__
    else:
        report_dict["Extended Measurement Or Fact"] = None

    # add errors
    report_dict["Errors"] = None
    report_dict["Missing Required Columns?"] = False
    report_dict["Missing Columns Events"] = None
    report_dict["Missing Columns Occurrence"] = None
    report_dict["Missing Columns Multimedia"] = None
    report_dict["Missing Columns eMoF"] = None
    report_dict["Incorrect DwC Terms Events"] = None
    report_dict["Incorrect DwC Terms Occurrence"] = None
    report_dict["Incorrect DwC Terms Multimedia"] = None
    report_dict["Incorrect DwC Terms eMoF"] = None
    report_dict["Data Missing/Invalid?"] = False

    # check taxonomy report 
    if report_dict["Occurrences"]["taxonomy_report"] is not None:
        if report_dict["Occurrences"]["taxonomy_report"].has_invalid_taxa:
            if report_dict['Errors'] is not None:
                report_dict['Errors'].append("There are some invalid taxa according to the backbone you are comparing against.")
            else:
                report_dict['Errors'] = ["There are some invalid taxa according to the backbone you are comparing against."]      
    else:
        report_dict['Errors'] = ["A taxonomy report could not be generated, likely because the column 'scientificName' is not in your column names."]      

    # check if all required columns are present; add them to Missing Columns
    for report_type in ["Events Report","Occurrences","Multimedia","Extended Measurement Or Fact"]:
        
        # check if report exists
        if report_dict[report_type]:

            if not report_dict[report_type]["all_required_columns_present"]:
                
                if report_dict['Errors'] is not None and "You are missing required columns in your data." not in report_dict["Errors"]:
                    report_dict['Errors'].append("You are missing required columns in your data.")
                elif report_dict['Errors'] is None:
                    report_dict['Errors'] = ["You are missing required columns in your data."]      

                if report_dict[report_type]["missing_columns"] is not None:
                    for x in report_dict[report_type]["missing_columns"]:
                        if report_type == "Events Report":
                            if report_dict["Missing Columns Events"] is None:
                                report_dict["Missing Columns Events"] = [x]
                            else:
                                report_dict["Missing Columns Events"].append(x)
                        elif report_type == "Occurrences":
                            if report_dict["Missing Columns Occurrence"] is None:
                                report_dict["Missing Columns Occurrence"] = [x]
                            else:
                                report_dict["Missing Columns Occurrence"].append(x)
                        elif report_type == "Multimedia":
                            if report_dict["Missing Columns Multimedia"] is None:
                                report_dict["Missing Columns Multimedia"] = [x]
                            else:
                                report_dict["Missing Columns Multimedia"].append(x)
                        else:
                            if report_dict["Missing Columns eMoF"] is None:
                                report_dict["Missing Columns eMoF"] = [x]
                            else:
                                report_dict["Missing Columns eMoF"].append(x)
                    
            if report_type == "Occurrences":
                if report_dict["Occurrences"]['taxonomy_report'] is None:
                    if report_dict["Missing Columns Occurrence"] is None:
                        report_dict["Missing Columns Occurrence"] = ["scientificName","vernacularName","genus","family","order","class","phylum","kingdom"]
                    else:
                        for y in ["scientificName","vernacularName","genus","family","order","class","phylum","kingdom"]:
                            if y not in report_dict["Missing Columns Occurrence"]:
                                report_dict["Missing Columns Occurrence"].append(y)
            
            if report_dict[report_type]['incorrect_dwc_terms']:

                # something
                if report_dict['Errors'] is not None:
                    if "Some of your columns do not match the current Darwin Core Standard." not in report_dict['Errors']:
                        report_dict['Errors'].append("Some of your columns do not match the current Darwin Core Standard.")
                else:
                    report_dict['Errors'] = ["Some of your columns do not match the current Darwin Core Standard."]  

                if report_dict[report_type]["incorrect_dwc_terms"] is not None:
                    for x in report_dict[report_type]["incorrect_dwc_terms"]:
                        if report_type == "Events Report":
                            if report_dict["Incorrect DwC Terms Events"] is None:
                                report_dict["Incorrect DwC Terms Events"] = [x]
                            else:
                                report_dict["Incorrect DwC Terms Events"].append(x)
                        elif report_type == "Occurrences":
                            if report_dict["Incorrect DwC Terms Occurrence"] is None:
                                report_dict["Incorrect DwC Terms Occurrence"] = [x]
                            else:
                                report_dict["Incorrect DwC Terms Occurrence"].append(x)
                        elif report_type == "Multimedia":
                            if report_dict["Incorrect DwC Terms Multimedia"] is None:
                                report_dict["Incorrect DwC Terms Multimedia"] = [x]
                            else:
                                report_dict["Incorrect DwC Terms Multimedia"].append(x)
                        else:
                            if report_dict["Incorrect DwC Terms eMoF"] is None:
                                report_dict["Incorrect DwC Terms eMoF"] = [x]
                            else:
                                report_dict["Incorrect DwC Terms eMoF"].append(x)

        if report_dict[report_type] is not None:
            if 'datetime_report' in report_dict[report_type]:
                if report_dict[report_type]['datetime_report'] is not None:
                    if report_dict[report_type]['datetime_report'].has_invalid_datetime:
                        if report_dict['Errors'] is not None:
                            report_dict['Errors'].append("Your datetime format in {} is not in YYYY-MM-DD or iso format.".format(report_type))
                        else:
                            report_dict['Errors'] = ["Your datetime format in {} is not in YYYY-MM-DD or iso format.".format(report_type)]      

    # check pass/fail based on errors and warnings
    if report_dict["Errors"] is None:
        report_dict["Pass/Fail"] = "Pass"

    # # write report to file
    # if verbose:
    #     report_file = open("./report_verbose.md","w")
    # else:
    #     report_file = open("./report_basic.md","w")

    # print report
    if print_to_screen:
        print("Archive Report\n---------------------")
        print("{}: {}".format("Pass/Fail",report_dict["Pass/Fail"]))
        print("{}: {}".format("Data Type",report_dict["Data Type"]))
        for x in ["Errors","Missing Columns Occurrence","Missing Columns Events",
                  "Missing Columns Multimedia","Missing Columns eMoF","Incorrect DwC Terms Events",
                  "Incorrect DwC Terms Occurrence","Incorrect DwC Terms Multimedia",
                  "Incorrect DwC Terms eMoF"]:
            if report_dict[x]:
                if report_dict is not None:
                    print("{}:".format(x))
                    for e in report_dict[x]:
                        if x == "Errors":
                            print("\t- {}".format(e))
                        else:
                            print("\t{}".format(e))
                else:
                    print("{}: None".format(x))
            # else:
            #     print("{}: None".format(x))

        # --------------------------------------
        # below this, make verbose option?
        # --------------------------------------

        # Events report
        if report_dict["Events Report"] is not None:
            print("\nEvents Report\n---------------------")
            print("Number of Events: {}".format(report_dict["Events Report"]['record_count']))
            print("Datetime Report:")
            print("\tHas invalid datetime: {}".format(report_dict["Events Report"]['datetime_report'].has_invalid_datetime))
            print("\tNumber of invalid datetimes: {}".format(report_dict["Events Report"]['datetime_report'].num_invalid_datetime))
            
            # Counts of entries in each column
            if report_dict["Events Report"]["column_counts"]:
                print("Column counts:")
                for e in report_dict["Events Report"]["column_counts"]:
                    print("\t{}: {}".format(e,report_dict["Events Report"]["column_counts"][e]))
            
        # Start Occurrence Report
        print("\nOccurrence Report\n---------------------")
        
        # Coordinates Report
        if report_dict["Occurrences"]['coordinates_report']:
            print("Coordinates Report:")
            print("\tData has coordinate fields?: {}".format(report_dict["Occurrences"]['coordinates_report'].has_coordinates_fields))
            print("\tInvalid latitude count: {}".format(report_dict["Occurrences"]['coordinates_report'].invalid_decimal_latitude_count))
            print("\tInvalid longitude count: {}".format(report_dict["Occurrences"]['coordinates_report'].invalid_decimal_longitude_count))
        
        # DateTime Report
        if report_dict["Occurrences"]['datetime_report']:
            print("Datetime Report:")
            print("\tHas invalid datetime: {}".format(report_dict["Occurrences"]['datetime_report'].has_invalid_datetime))
            print("\tNumber of invalid datetimes: {}".format(report_dict["Occurrences"]['datetime_report'].num_invalid_datetime))

        # Taxonomy Report
        if report_dict["Occurrences"]['taxonomy_report'] is not None:
            print("Taxonomy Report:")
            print("\tInvalid taxon present: {}".format(report_dict["Occurrences"]['taxonomy_report'].has_invalid_taxa))
            print("\tValid Taxon count: {}".format(report_dict["Occurrences"]['taxonomy_report'].valid_taxon_count))
            if report_dict["Occurrences"]['taxonomy_report'].has_invalid_taxa:
                print("\tUnrecognised taxa:\n")
                print(pd.DataFrame(report_dict["Occurrences"]['taxonomy_report'].unrecognised_taxa))
                print()
        else:
            print("Taxonomy Report:")
            print("\tCould not do a taxonomic classification because 'scientificName' is likely missing from your columns.")

        # Counts of entries in each column
        if report_dict["Occurrences"]["column_counts"]:
            print("Column counts:")
            for e in report_dict["Occurrences"]["column_counts"]:
                print("\t{}: {}".format(e,report_dict["Occurrences"]["column_counts"][e]))

        # Now go on to the multimedia report
        if report_dict["Multimedia"] is not None:

            # print title
            print("\nMultimedia Report\n---------------------")

            # record count
            print("{}: {}".format("Number of Multimedia Records",report_dict["Multimedia"]["record_count"]))

            # column counts
            print("Column counts:")
            for c in report_dict["Multimedia"]['column_counts']:
                print("\t{}: {}".format(c,report_dict["Multimedia"]['column_counts'][c]))

        if report_dict['Extended Measurement Or Fact'] is not None:
            print("\nExtended Measurement Or Fact Report\n---------------------")
            print("{}: {}".format("Number of eMoF Records",report_dict["Extended Measurement Or Fact"]["record_count"]))
            print("Column counts:")
            for c in report_dict["Extended Measurement Or Fact"]['column_counts']:
                print("\t{}: {}".format(c,report_dict["Extended Measurement Or Fact"]['column_counts'][c]))

    else:
        print("Need to do something about this")
        
    # do something about this...
    # report_file.close()         