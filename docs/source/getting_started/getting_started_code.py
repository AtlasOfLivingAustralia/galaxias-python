import pandas as pd
import galaxias
import sys

# set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

stop = int(sys.argv[1])

my_dict = {
    'latitude': [-35.3,-35.3],
    'longitude': [149.0,149.0],
    'date': ['14-01-2023','15-01-2023'],
    'time': ['10:23','11:25'],
    'species': ['Callocephalon fimbriatum','Eolophus roseicapilla'],
    'location_id': ['ARD001','ARD001']
}

my_data = pd.DataFrame(my_dict)

if stop == 1:
    print(my_data)
    sys.exit()

if stop == 2:
    galaxias.suggest_workflow(occurrences=my_data)
    sys.exit()

# basic requirements of Darwin Core
my_data = galaxias.set_occurrences(occurrences=my_data,
                                   occurrenceID = 'sequential',
                                   basisOfRecord = 'HumanObservation')
# place and time
my_data = galaxias.set_coordinates(dataframe=my_data,
                                   decimalLatitude = 'latitude', 
                                   decimalLongitude = 'longitude')
my_data = galaxias.set_locality(dataframe=my_data,
                                country = "Australia", 
                                locality = "Canberra")
my_data = galaxias.set_datetime(dataframe=my_data,
                                eventDate = 'date',
                                eventTime = 'time',
                                string_to_datetime=True,
                                dayfirst=True,
                                yearfirst=False,
                                time_format='mixed')
# taxonomy
my_data = galaxias.set_scientific_name(dataframe=my_data,
                                       scientificName = 'species', 
                                       taxonRank = 'species')
my_data = galaxias.set_taxonomy(dataframe=my_data,
                                kingdom = 'Animalia',
                                family = 'Cacatuidae') 

if stop == 3:
    print(my_data)
    sys.exit()

occ_terms = list(galaxias.occurrence_terms())
occ_terms_dwca = list(set(occ_terms).intersection(list(my_data.columns)))
my_data_final = my_data[occ_terms_dwca]

if stop == 4:
    print(my_data_final)
    sys.exit()