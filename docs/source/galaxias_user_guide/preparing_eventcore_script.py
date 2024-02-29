import galaxias
import pandas as pd
import sys

# get option
data_type = sys.argv[1]
stopping_point = sys.argv[2]

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# --------------------------------------------------------
# Part 1
# --------------------------------------------------------

# read in data
if data_type == "event":
    events = pd.read_csv("galaxias_user_guide/events.csv")
    occurrences = pd.read_csv("galaxias_user_guide/occurrences_event_nomulti.csv")
    my_dwca = galaxias.dwca(events=events,occurrences=occurrences)
elif data_type == "event_multi":
    events = pd.read_csv("galaxias_user_guide/events.csv")
    occurrences = pd.read_csv("galaxias_user_guide/occurrences_event_multi.csv")
    multimedia = pd.read_csv("galaxias_user_guide/multimedia_event.csv")
    my_dwca = galaxias.dwca(events=events,occurrences=occurrences,multimedia=multimedia)
elif data_type == "event_emof":
    events = pd.read_csv("galaxias_user_guide/events.csv")
    occurrences = pd.read_csv("galaxias_user_guide/occurrences_event_multi.csv")
    emof = pd.read_csv("galaxias_user_guide/extendedMeasurementOrFact.csv")
    my_dwca = galaxias.dwca(events=events,occurrences=occurrences,emof=emof)
elif data_type == "event_multi_emof":
    events = pd.read_csv("galaxias_user_guide/events.csv")
    occurrences = pd.read_csv("galaxias_user_guide/occurrences_event_multi.csv")
    multimedia = pd.read_csv("galaxias_user_guide/multimedia_event.csv")
    emof = pd.read_csv("galaxias_user_guide/extendedMeasurementOrFact.csv")
    my_dwca = galaxias.dwca(events=events,occurrences=occurrences,
                            multimedia=multimedia,emof=emof)
else:
    raise ValueError("{} is not an option.".format(data_type))

# generate initial data report and exit
if stopping_point == "1":
    my_dwca.generate_data_report()
    sys.exit()

# if stopping_point == "rename1":
#     print(my_dwca.occurrences.head())
#     sys.exit()

# temp_occurrences = my_dwca.occurrences.rename(
#     columns = {
#         "Species": "scientificName",
#         "Latitude": "decimalLatitude",
#         "Longitude": "decimalLongitude",
#         "Collection_date": "eventDate",
#     }
# )
# if stopping_point == "rename2":
#     print(temp_occurrences.head())
#     sys.exit()

# my_dwca.occurrences = temp_occurrences
# if stopping_point == "rename3":
#     print(my_dwca.occurrences.head())
#     sys.exit()

# if stopping_point == "rename4":
#     print(my_dwca.generate_data_report())
#     sys.exit()


# # --------------------------------------------------------
# # Part 2
# # --------------------------------------------------------

# if "check_taxon" in stopping_point or stopping_point == "add_taxon":

#     if stopping_point == "check_taxon1":
#         print(my_dwca.generate_data_report())
#         sys.exit()

#     name_changes = {
#         "Eucalyptus camaldulensis var. obtusa": "Eucalyptus camaldulensis subsp. obtusa",
#         "Acacia murayana": "Acacia murrayana",
#         "Eucalyptus sclerophylla": "Eucalyptus racemosa"
#     }
#     for name in name_changes:
#         my_dwca.occurrences['scientificName'] = my_dwca.occurrences['scientificName'].replace(regex=name, value=name_changes[name])

#     if stopping_point == "check_taxon":
#         print(my_dwca.occurrences)
#         sys.exit()

# if stopping_point == "add_taxon":
#     my_dwca.add_taxonomic_information()
#     print(my_dwca.occurrences.head())
#     sys.exit()

# if "add_reqs" in stopping_point:

#     if stopping_point == "add_reqs1":
#         my_dwca.generate_data_report()
#         sys.exit()

#     my_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
#     my_dwca.occurrences["geodeticDatum"] = "WGS84"
#     my_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"

#     if stopping_point == "add_reqs2":
#         print(my_dwca.occurrences.head())
#         sys.exit()

#     my_dwca.add_unique_occurrence_IDs(column_name="occurrenceID")

#     if stopping_point == "add_reqs3":
#         print(my_dwca.occurrences.head())
#         sys.exit()

# if stopping_point == "final":

#     # name changes
#     name_changes = {
#         "Eucalyptus camaldulensis var. obtusa": "Eucalyptus camaldulensis subsp. obtusa",
#         "Acacia murayana": "Acacia murrayana",
#         "Eucalyptus sclerophylla": "Eucalyptus racemosa"
#     }
#     for name in name_changes:
#         my_dwca.occurrences['scientificName'] = my_dwca.occurrences['scientificName'].replace(regex=name, value=name_changes[name])

#     # add higher taxon
#     my_dwca.add_taxonomic_information()

#     # add required columns
#     my_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
#     my_dwca.occurrences["geodeticDatum"] = "WGS84"
#     my_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"

#     # add occurrence IDs
#     my_dwca.add_unique_occurrence_IDs(column_name="occurrenceID")

#     my_dwca.generate_data_report(verbose=True)

#     ### TODO: add this step
#     temp_occurrences = my_dwca.occurrences.rename(
#         columns = {
#             "classs": "class",
#         }
#     )
#     my_dwca.occurrences = temp_occurrences

#     my_dwca.occurrences.to_csv("galaxias_user_guide/occurrences_dwc_clean.csv",index=False)
#     sys.exit()
