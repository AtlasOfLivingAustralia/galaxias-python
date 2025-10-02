import galaxias
import pandas as pd

import os
occurrences = pd.read_csv('galaxias_user_guide/data/dummy-dataset-sb.csv')
occurrences.columns = map(str.lower, occurrences.columns)

# -----------------------------------------------------------------------------
# set_occurrences
# -----------------------------------------------------------------------------
occurrences = galaxias.set_scientific_name(dataframe=occurrences,
                                           scientificName = 'species')
occurrences = galaxias.set_coordinates(dataframe=occurrences,
                                       decimalLatitude = 'lat',
                                       decimalLongitude = 'lon',
                                       geodeticDatum = 'WGS84',
                                       coordinateUncertaintyInMeters = 30)
occurrences = galaxias.set_datetime(dataframe=occurrences,
                                    eventDate = 'date',
                                    string_to_datetime=True,
                                    yearfirst = True)
occurrences = galaxias.set_occurrences(occurrences=occurrences,
                                       occurrenceID = ['sequential','site','landscape'],
                                       basisOfRecord = 'HumanObservation')
occurrences = galaxias.set_individual_traits(dataframe=occurrences)

occ_terms = list(galaxias.occurrence_terms())
occ_terms_dwca = list(set(occ_terms).intersection(list(occurrences.columns)))
occurrences_final = occurrences[occ_terms_dwca]

# write out data
galaxias.use_data(occurrences=occurrences_final)

# create metadata
galaxias.use_metadata_template()
galaxias.use_metadata()

my_dwca = galaxias.dwca(occurrences='./data-publish/occurrences.csv')
print(my_dwca.occurrences)

# create archive
my_dwca.build_archive(print_report=False)

# validate archive
my_dwca.check_archive(username = "acbuyan",email = "amanda.buyan@csiro.au",
                         password = "galaxias-gbif-testing-login")