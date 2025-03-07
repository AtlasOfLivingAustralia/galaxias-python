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
my_dwca=galaxias.dwca(occurrences="galaxias_user_guide/data/occurrences_event_nomulti.csv",
                      events="galaxias_user_guide/data/events_use.csv")

# generate initial data report and exit
if stopping_point == "1":
    my_dwca.check_dataset()
    sys.exit()

if stopping_point == "2":
    my_dwca.suggest_workflow()
    sys.exit()

if stopping_point == "4":
    my_dwca.use_events(eventType='type',samplingProtocol='Observation',Event='name')
    print(my_dwca.events.head())
    sys.exit()

if stopping_point == "5":
    my_dwca.use_events(eventType='type',samplingProtocol='Observation',Event='name',
                       event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    print(my_dwca.events.head())
    sys.exit()

if stopping_point == "6":
    my_dwca.use_events(eventType='type',samplingProtocol='Observation',Event='name',
                                    event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    my_dwca.check_dataset()
    sys.exit()

if stopping_point == "7":
    my_dwca.use_events(eventType='type',samplingProtocol='Observation',Event='name',
                                    event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    my_dwca.suggest_workflow()
    sys.exit()

if stopping_point == "8":
    my_dwca.use_datetime(check_events=True)
    import sys
    sys.exit()

if stopping_point == "9":
    my_dwca.use_datetime(check_events=True,eventDate='Collection_date')
    print(my_dwca.events.head())
    import sys
    sys.exit()

if stopping_point == "10":
    my_dwca.use_datetime(check_events=True,eventDate='Collection_date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    print(my_dwca.events.head())
    import sys
    sys.exit()

if stopping_point == "11":
    my_dwca.use_datetime(check_events=True,eventDate='Collection_date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    my_dwca.check_dataset()
    import sys
    sys.exit()

if stopping_point == "12":
    my_dwca.use_datetime(check_events=True,eventDate='Collection_date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    my_dwca.suggest_workflow()
    import sys
    sys.exit()

if stopping_point == "13":
    events = my_dwca.use_events(dataframe=events,
                             eventType='type',
                             samplingProtocol='Observation',
                             Event='name',
                             event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    events = my_dwca.use_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    occ = my_dwca.use_occurrences(dataframe=occ,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='PRESENT',
                                  occurrenceID=True)
    occ = my_dwca.use_scientific_name(dataframe=occ,
                                      scientificName='Species')
    occ = my_dwca.use_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude',
                                  geodeticDatum='WGS84',
                                  coordinatePrecision=0.1)
    occ = my_dwca.use_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    print(my_dwca.use_occurrences(dataframe=occ,add_eventID=True,events=events,eventType='Observation'))

if stopping_point == "14":
    events = my_dwca.use_events(dataframe=events,
                             eventType='type',
                             samplingProtocol='Observation',
                             Event='name',
                             event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    events = my_dwca.use_datetime(dataframe=events,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    occ = my_dwca.use_occurrences(dataframe=occ,
                                  basisOfRecord='HumanObservation',
                                  occurrenceStatus='PRESENT',
                                  occurrenceID=True,
                                  add_eventID=True,
                                  events=events,
                                  eventType='Observation')
    occ = my_dwca.use_scientific_name(dataframe=occ,
                                      scientificName='Species')
    occ = my_dwca.use_coordinates(dataframe=occ,
                                  decimalLatitude='Latitude',
                                  decimalLongitude='Longitude',
                                  geodeticDatum='WGS84',
                                  coordinatePrecision=0.1)
    occ = my_dwca.use_datetime(dataframe=occ,
                               eventDate='Collection_date',
                               string_to_datetime=True,
                               yearfirst=False,
                               dayfirst=True)
    print(my_dwca.check_dataset(occurrences=occ,events=events))


# temp_emof = my_dwca.emof.rename(
#     columns = {
#         "measurement": "measurementType",
#         "value": "measurementValue",
#         "unit": "measurementUnit",
#         "error": "measurementAccuracy"
#     }
# )