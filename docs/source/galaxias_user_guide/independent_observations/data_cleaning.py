import galaxias
import pandas as pd
import sys

# set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# get arguments
stop = int(sys.argv[1])
my_dwca = galaxias.dwca(occurrences = 'galaxias_user_guide/data/occurrences_dwc.csv', print_notices = False)
    
# -----------------------------------------------------------------------------
# set_occurrences
# -----------------------------------------------------------------------------
if stop == 1:
    # data
    print(my_dwca.check_dataset())
    sys.exit()

if stop == 2:
    print(my_dwca.suggest_workflow())
    sys.exit()

if stop == 3:
    my_dwca.set_occurrences(basisOfRecord='HumanObservation')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 4:
    my_dwca.set_occurrences(basisOfRecord='HumanObservation',occurrenceID='random')
    print(my_dwca.occurrences.head())
    sys.exit()

if stop == 5:
    my_dwca.set_occurrences(basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',occurrenceID='random')
    print(my_dwca.occurrences.head())
    sys.exit()
    
if stop == 6:
    my_dwca.set_occurrences(basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',occurrenceID='random')
    my_dwca.check_dataset()
    sys.exit()

if stop == 7:
    my_dwca.set_occurrences(basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',occurrenceID='random')
    my_dwca.suggest_workflow()

# -----------------------------------------------------------------------------
# set_scientific_name
# -----------------------------------------------------------------------------
if stop == 11:
    my_dwca.set_scientific_name(scientificName='Species')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 12:
    my_dwca.set_scientific_name(scientificName='Species')
    my_dwca.check_dataset()
    sys.exit() 

if stop == 13:
    my_dwca.set_scientific_name(scientificName='Species')
    my_dwca.suggest_workflow()
    sys.exit() 

# -----------------------------------------------------------------------------
# set_coordinates
# -----------------------------------------------------------------------------
if stop == 15:
    my_dwca.set_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 16:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.set_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 17:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.set_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',geodeticDatum='WGS84')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 18:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.set_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',geodeticDatum='WGS84',
                            coordinatePrecision=0.1)
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 19:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.set_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',
                            geodeticDatum='WGS84',coordinatePrecision=0.1)
    my_dwca.check_dataset()
    sys.exit() 

if stop == 20:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.set_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',
                            geodeticDatum='WGS84',coordinatePrecision=0.1)
    my_dwca.suggest_workflow()
    sys.exit() 

# -----------------------------------------------------------------------------
# set_datetime
# -----------------------------------------------------------------------------
if stop == 22:
    my_dwca.set_datetime(eventDate='Collection_date')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 23:
    my_dwca.set_datetime(eventDate='Collection_date',
                         string_to_datetime=True,
                         yearfirst=False,
                         dayfirst=True)
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 24:
    my_dwca.set_datetime(eventDate='Collection_date',
                         string_to_datetime=True,
                         yearfirst=False,
                         dayfirst=True)
    print(my_dwca.check_dataset())
    sys.exit() 

if stop == 25:
    my_dwca.set_datetime(eventDate='Collection_date',
                         string_to_datetime=True,
                         yearfirst=False,
                         dayfirst=True)
    print(my_dwca.suggest_workflow())
    sys.exit() 

# -----------------------------------------------------------------------------
# set_abundance
# -----------------------------------------------------------------------------
occ = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
                   'latitude': [-35.310, '-35.273'], 
                   'longitude': [149.125, 149.133], 
                   'date': ['14-01-2023', '15-01-2023'], 
                   'status': ['present', 'present'],
                   'count': [2,1]})

temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)

if stop == 27:
    temp_dwca.set_abundance(individualCount='count')
    print(temp_dwca.occurrences.head())
    sys.exit() 

# -----------------------------------------------------------------------------
# set_locality
# -----------------------------------------------------------------------------
occ = pd.read_csv('galaxias_user_guide/data/occurrences_dwc.csv')

temp_dwca = galaxias.dwca(occurrences=occ, print_notices = False)

if stop == 29:
    temp_dwca.set_locality(continent='Australia')
    print(temp_dwca.occurrences.head())
    sys.exit() 

if stop == 30:
    temp_dwca.set_locality(continent='Oceania',country='Australia')
    print(temp_dwca.occurrences.head())
    sys.exit() 

# -----------------------------------------------------------------------------
# set_taxonomy
# -----------------------------------------------------------------------------
if stop == 31:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)
    temp_dwca.set_taxonomy(kingdom='Animalia',phylum='Chordata',taxon_class='Aves',
                               order='Psittaciformes',family='Cacatuidae',genus='Eolophus',
                               specificEpithet='roseicapilla',vernacularName='Galah')
    print(temp_dwca.occurrences.head())
    sys.exit()

# -----------------------------------------------------------------------------
# set_collection
# -----------------------------------------------------------------------------
if stop == 32:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)
    temp_dwca.set_collection(datasetID='b15d4952-7d20-46f1-8a3e-556a512b04c5',
                             datasetName='Lacey Ctenomys Recaptures',catalogNumber='2008.1334')
    print(temp_dwca.occurrences.head())
    sys.exit()

# -----------------------------------------------------------------------------
# set_individual_traits
# -----------------------------------------------------------------------------
if stop == 33:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)
    temp_dwca.set_individual_traits(individualID=['123456','123457'],
                                        lifeStage='adult',sex=['male','female'],
                                        vitality='alive',reproductiveCondition='not reproductive')
    print(temp_dwca.occurrences.head())
    sys.exit()
    
# -----------------------------------------------------------------------------
# set_license
# -----------------------------------------------------------------------------
if stop == 34:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)
    temp_dwca.set_license(license=['CC-BY 4.0 (Int)', 'CC-BY-NC 4.0 (Int)'],
                              rightsHolder='The Regents of the University of California',
                              accessRights=['','not-for-profit use only'])
    print(temp_dwca.occurrences.head())
    sys.exit()
    
# -----------------------------------------------------------------------------
# creating IDs
# -----------------------------------------------------------------------------
if stop == 35:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                        'latitude': [-35.310, -35.273], 
                        'longitude': [149.125, 149.133], 
                        'date': ['14-01-2023', '15-01-2023']})
    temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)
    temp_dwca.set_occurrences(occurrenceID='random')
    print(temp_dwca.occurrences.head())
    sys.exit()

if stop == 36:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                        'latitude': [-35.310, -35.273], 
                        'longitude': [149.125, 149.133], 
                        'date': ['14-01-2023', '15-01-2023']})
    temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)
    temp_dwca.set_occurrences(occurrenceID='sequential')
    print(temp_dwca.occurrences.head())
    sys.exit()

if stop == 37:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                        'latitude': [-35.310, -35.273], 
                        'longitude': [149.125, 149.133], 
                        'date': ['14-01-2023', '15-01-2023']})
    temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)
    temp_dwca.set_occurrences(occurrenceID=['sequential','date'])
    print(temp_dwca.occurrences.head())
    sys.exit()

if stop == 38:
    occ = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                        'latitude': [-35.310, -35.273], 
                        'longitude': [149.125, 149.133], 
                        'date': ['14-01-2023', '15-01-2023']})
    temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)
    temp_dwca.set_occurrences(occurrenceID=['date','random'])
    print(temp_dwca.occurrences.head())
    sys.exit()

# -----------------------------------------------------------------------------
# final
# -----------------------------------------------------------------------------
my_dwca = galaxias.dwca(occurrences = 'galaxias_user_guide/data/occurrences_dwc.csv', print_notices = False)

if stop == 39:
    my_dwca.set_occurrences(basisOfRecord='HumanObservation',occurrenceID='random')
    my_dwca.set_scientific_name(scientificName='Species')
    my_dwca.set_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',
                            geodeticDatum='WGS84',coordinatePrecision=0.1)
    my_dwca.set_datetime(eventDate='Collection_date',string_to_datetime=True,yearfirst=False,
                         dayfirst=True)
    my_dwca.check_dataset()
    import sys
    sys.exit()