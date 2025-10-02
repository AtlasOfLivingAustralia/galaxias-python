import galaxias
import pandas as pd
import sys

# set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# get arguments
stop = int(sys.argv[1])
occurrences = pd.read_csv('galaxias_user_guide/data/dummy-dataset-sb.csv')
# my_dwca = galaxias.dwca(occurrences = , print_notices = False)
occurrences.columns = map(str.lower, occurrences.columns)

# -----------------------------------------------------------------------------
# set_occurrences
# -----------------------------------------------------------------------------
if stop == 1:
    print(occurrences)
    sys.exit()

if stop == 2:
    galaxias.suggest_workflow(occurrences=occurrences)
    sys.exit()

occurrences = galaxias.set_scientific_name(dataframe=occurrences,
                                           scientificName = 'species')
occurrences = galaxias.set_coordinates(dataframe=occurrences,
                                       decimalLatitude = 'lat',
                                       decimalLongitude = 'lon')
occurrences = galaxias.set_datetime(dataframe=occurrences,
                                    eventDate = 'date',
                                    string_to_datetime=True,
                                    yearfirst = True)

if stop == 3:
    galaxias.suggest_workflow(occurrences=occurrences)
    sys.exit() 

occurrences = galaxias.set_occurrences(occurrences=occurrences,
                                       occurrenceID = ['sequential','site','landscape'],
                                       basisOfRecord = 'HumanObservation')
occurrences = galaxias.set_coordinates(dataframe=occurrences,geodeticDatum = 'WGS84',
                                       coordinateUncertaintyInMeters = 30)
occurrences = galaxias.set_individual_traits(dataframe=occurrences)

if stop == 4:
    galaxias.suggest_workflow(occurrences=occurrences)
    sys.exit() 

occ_terms = list(galaxias.occurrence_terms())
occ_terms_dwca = list(set(occ_terms).intersection(list(occurrences.columns)))
occurrences_final = occurrences[occ_terms_dwca]
occurrences_final

if stop == 5:
    print(occurrences_final)
    sys.exit()