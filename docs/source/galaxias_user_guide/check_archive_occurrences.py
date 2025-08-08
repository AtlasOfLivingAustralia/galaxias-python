import galaxias

my_dwca = galaxias.dwca(occurrences = 'galaxias_user_guide/data/occurrences_dwc.csv', print_notices = False)

# set all occurrences
my_dwca.set_occurrences(basisOfRecord='HumanObservation',occurrenceID='random')
my_dwca.set_scientific_name(scientificName='Species')
my_dwca.set_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',
                        geodeticDatum='WGS84',coordinatePrecision=0.1)
my_dwca.set_datetime(eventDate='Collection_date',string_to_datetime=True,yearfirst=False,
                        dayfirst=True)

# create metadata
my_dwca.write_eml()

# create archive
my_dwca.build_archive(print_report=False)

# validate archive
my_dwca.check_archive(username = "acbuyan",email = "amanda.buyan@csiro.au",
                         password = "galaxias-gbif-testing-login")