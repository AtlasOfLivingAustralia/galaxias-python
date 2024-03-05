import galaxias
import pandas as pd
import sys

# get option
stopping_point = sys.argv[1]
if len(sys.argv) > 1:
    data_type = True #sys.argv[2]
else:
    data_type = False

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# --------------------------------------------------------
# Part 1
# --------------------------------------------------------

# read in data
events = pd.read_csv("galaxias_user_guide/events.csv")
occurrences = pd.read_csv("galaxias_user_guide/occurrences_event_multi.csv")
# multimedia = pd.read_csv("galaxias_user_guide/multimedia_event.csv")
# emof = pd.read_csv("galaxias_user_guide/extendedMeasurementOrFact.csv")
my_dwca = galaxias.dwca(events=events,occurrences=occurrences) #,
                        # multimedia=multimedia,emof=emof)

# generate initial data report and exit
if stopping_point == "1":
    my_dwca.generate_data_report()
    sys.exit()
    # if not data_type:
    #     my_dwca.generate_data_report()
    #     sys.exit()
    # else:
    #     events = pd.read_csv("galaxias_user_guide/events.csv")
    #     occurrences = pd.read_csv("galaxias_user_guide/occurrences_event_multi.csv")
    #     my_dwca = galaxias.dwca(events=events,occurrences=occurrences)
    #     my_dwca.generate_data_report()
    #     sys.exit()

if stopping_point == "2":
    print(my_dwca.occurrences.head())
    sys.exit()

temp_occurrences = my_dwca.occurrences.rename(
    columns = {
        "Species": "scientificName",
        "Latitude": "decimalLatitude",
        "Longitude": "decimalLongitude",
        "Collection_date": "eventDate",
        "number_birds": "individualCount"
    }
)
if stopping_point == "3":
    print(temp_occurrences.head())
    sys.exit()

my_dwca.occurrences = temp_occurrences

if stopping_point == "4":
    print(my_dwca.occurrences.head())
    sys.exit()

# Events
if stopping_point == "5":
    print(my_dwca.events.head())

temp_events = my_dwca.events.rename(
    columns = {
        "eventName": "Event",
    }
)

my_dwca.events = temp_events

if stopping_point == "5":
    print()
    print()
    print(my_dwca.events.head())
    sys.exit()


# # Multimedia
# if stopping_point == "6":
#     print(my_dwca.multimedia.head())

# temp_multimedia = my_dwca.multimedia.rename(
#     columns = {
#         "photo": "identifier",
#     }
# )

# my_dwca.multimedia = temp_multimedia

# if stopping_point == "6":
#     print()
#     print()
#     print(my_dwca.multimedia.head())
#     sys.exit()

# # emof
# if stopping_point == "7":
#     print(my_dwca.emof.head())

# temp_emof = my_dwca.emof.rename(
#     columns = {
#         "measurement": "measurementType",
#         "value": "measurementValue",
#         "unit": "measurementUnit",
#         "error": "measurementAccuracy"
#     }
# )

# my_dwca.emof = temp_emof

# if stopping_point == "7":
#     print()
#     print()
#     print(my_dwca.emof.head())
#     sys.exit()

if stopping_point == "8":
    print(my_dwca.generate_data_report())

# --------------------------------------------------------
# Part 2
# --------------------------------------------------------
    
if stopping_point == "9":
    print("here")
    print(my_dwca.generate_data_report())
    sys.exit()

name_changes = {
    "Eucalyptus camaldulensis var. obtusa": "Eucalyptus camaldulensis subsp. obtusa",
    "Acacia murayana": "Acacia murrayana",
    "Eucalyptus sclerophylla": "Eucalyptus racemosa"
}

for name in name_changes:
    my_dwca.occurrences['scientificName'] = my_dwca.occurrences['scientificName'].replace(regex=name, value=name_changes[name])

if stopping_point == "10":
    print(my_dwca.occurrences)
    sys.exit()

if stopping_point == "11":
    my_dwca.add_taxonomic_information()
    print(my_dwca.occurrences.head())
    sys.exit()

'''
if "add_reqs" in stopping_point:

    if stopping_point == "add_reqs1":
        my_dwca.generate_data_report()
        sys.exit()

    my_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    my_dwca.occurrences["geodeticDatum"] = "WGS84"
    my_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"

    if stopping_point == "add_reqs2":
        print(my_dwca.occurrences.head())
        sys.exit()

    my_dwca.add_unique_occurrence_IDs(column_name="occurrenceID")

    if stopping_point == "add_reqs3":
        print(my_dwca.occurrences.head())
        sys.exit()

if stopping_point == "final":

    # name changes
    name_changes = {
        "Eucalyptus camaldulensis var. obtusa": "Eucalyptus camaldulensis subsp. obtusa",
        "Acacia murayana": "Acacia murrayana",
        "Eucalyptus sclerophylla": "Eucalyptus racemosa"
    }
    for name in name_changes:
        my_dwca.occurrences['scientificName'] = my_dwca.occurrences['scientificName'].replace(regex=name, value=name_changes[name])
'''