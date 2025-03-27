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
# Initialising and suggesting workflow
# --------------------------------------------------------

# read in data
my_dwca=galaxias.dwca(occurrences="galaxias_user_guide/data/occurrences_event_nomulti.csv",
                    events="galaxias_user_guide/data/events_use.csv",
                    working_dir="dwca_data_events",
                    print_notices=False)

# generate initial data report and exit
if stopping_point == "1":
    my_dwca.check_dataset()
    sys.exit()

if stopping_point == "2":
    my_dwca.suggest_workflow()
    sys.exit()

# --------------------------------------------------------
# Use events
# --------------------------------------------------------

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

# --------------------------------------------------------
# use_datetime
# --------------------------------------------------------

if stopping_point == "8":
    my_dwca.use_datetime(check_events=True)
    import sys
    sys.exit()

if stopping_point == "9":
    my_dwca.use_datetime(check_events=True,eventDate='date')
    print(my_dwca.events.head())
    import sys
    sys.exit()

if stopping_point == "10":
    my_dwca.use_datetime(check_events=True,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    print(my_dwca.events.head())
    import sys
    sys.exit()

if stopping_point == "11":
    my_dwca.use_datetime(check_events=True,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    my_dwca.check_dataset()
    import sys
    sys.exit()

if stopping_point == "12":
    my_dwca.use_datetime(check_events=True,eventDate='Collection_date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    my_dwca.suggest_workflow()
    import sys
    sys.exit()

# --------------------------------------------------------
# adding eventID to occurrences
# --------------------------------------------------------

if stopping_point == "13":
    my_dwca.use_events(eventType='type',
                       samplingProtocol='Observation',
                       Event='name',
                       event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.occurrences['Longitude'] = pd.to_numeric(my_dwca.occurrences['Longitude'],errors='coerce')
    my_dwca.use_datetime(check_events=True,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    my_dwca.use_occurrences(basisOfRecord='HumanObservation',
                            occurrenceStatus='PRESENT',
                            occurrenceID=True)
    my_dwca.use_scientific_name(scientificName='Species')
    my_dwca.use_coordinates(decimalLatitude='Latitude',
                            decimalLongitude='Longitude',
                            geodeticDatum='WGS84',
                            coordinatePrecision=0.1)
    my_dwca.use_datetime(eventDate='Collection_date',
                         string_to_datetime=True,
                         yearfirst=False,
                         dayfirst=True)
    my_dwca.use_occurrences(add_eventID=True,
                            eventType='Observation')
    print(my_dwca.occurrences.head())

# --------------------------------------------------------
# use_abundance
# --------------------------------------------------------
if stopping_point == '14':
    my_dwca.use_abundance(individualCount='number_birds')
    print(my_dwca.occurrences.head())

# --------------------------------------------------------
# use_locality
# --------------------------------------------------------
if stopping_point == '15':
    my_dwca.use_locality(check_events = True, locality='location')
    print(my_dwca.events.head())
# --------------------------------------------------------
# Passing dataset
# --------------------------------------------------------

if stopping_point == "16":
    my_dwca.use_events(eventType='type',
                       samplingProtocol='Observation',
                       Event='name',
                       event_hierarchy={1: "Site Visit", 2: "Sample", 3: "Observation"})
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.occurrences['Longitude'] = pd.to_numeric(my_dwca.occurrences['Longitude'],errors='coerce')
    my_dwca.use_datetime(check_events=True,eventDate='date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    my_dwca.use_occurrences(basisOfRecord='HumanObservation',
                            occurrenceID=True)
    my_dwca.use_scientific_name(scientificName='Species')
    my_dwca.use_coordinates(decimalLatitude='Latitude',
                            decimalLongitude='Longitude',
                            geodeticDatum='WGS84',
                            coordinatePrecision=0.1)
    my_dwca.use_datetime(eventDate='Collection_date',
                         string_to_datetime=True,
                         yearfirst=False,
                         dayfirst=True)
    my_dwca.use_occurrences(add_eventID=True,eventType='Observation')
    my_dwca.use_abundance(individualCount='number_birds')
    my_dwca.use_locality(check_events = True, locality='location')
    my_dwca.check_dataset()

# temp_emof = my_dwca.emof.rename(
#     columns = {
#         "measurement": "measurementType",
#         "value": "measurementValue",
#         "unit": "measurementUnit",
#         "error": "measurementAccuracy"
#     }
# )