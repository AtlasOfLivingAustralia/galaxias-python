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
# use_occurrences
# -----------------------------------------------------------------------------
if stop == 1:
    # data
    print(my_dwca.check_dataset())
    sys.exit()

if stop == 2:
    print(my_dwca.suggest_workflow())
    sys.exit()

if stop == 3:
    my_dwca.use_occurrences(basisOfRecord='HumanObservation')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 4:
    my_dwca.use_occurrences(basisOfRecord='HumanObservation',occurrenceID=True)
    print(my_dwca.occurrences.head())
    sys.exit()

if stop == 5:
    my_dwca.use_occurrences(basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',occurrenceID=True)
    print(my_dwca.occurrences.head())
    sys.exit()
    
if stop == 6:
    my_dwca.use_occurrences(basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',occurrenceID=True)
    my_dwca.check_dataset()
    sys.exit()

if stop == 7:
    my_dwca.use_occurrences(basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',occurrenceID=True)
    my_dwca.suggest_workflow()

# -----------------------------------------------------------------------------
# use_scientific_name
# -----------------------------------------------------------------------------
if stop == 11:
    my_dwca.use_scientific_name(scientificName='Species')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 12:
    my_dwca.use_scientific_name(scientificName='Species')
    my_dwca.check_dataset()
    sys.exit() 

if stop == 13:
    my_dwca.use_scientific_name(scientificName='Species')
    my_dwca.suggest_workflow()
    sys.exit() 

# -----------------------------------------------------------------------------
# use_coordinates
# -----------------------------------------------------------------------------
if stop == 15:
    my_dwca.use_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 16:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.use_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 17:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.use_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',geodeticDatum='WGS84')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 18:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.use_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',geodeticDatum='WGS84',
                            coordinatePrecision=0.1)
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 19:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.use_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',
                            geodeticDatum='WGS84',coordinatePrecision=0.1)
    my_dwca.check_dataset()
    sys.exit() 

if stop == 20:
    my_dwca.occurrences['Latitude'] = pd.to_numeric(my_dwca.occurrences['Latitude'],errors='coerce')
    my_dwca.use_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',
                            geodeticDatum='WGS84',coordinatePrecision=0.1)
    my_dwca.suggest_workflow()
    sys.exit() 

# -----------------------------------------------------------------------------
# use_datetime
# -----------------------------------------------------------------------------
if stop == 22:
    my_dwca.use_datetime(eventDate='Collection_date')
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 23:
    my_dwca.use_datetime(eventDate='Collection_date',
                         string_to_datetime=True,
                         yearfirst=False,
                         dayfirst=True)
    print(my_dwca.occurrences.head())
    sys.exit() 

if stop == 24:
    my_dwca.use_datetime(eventDate='Collection_date',
                         string_to_datetime=True,
                         yearfirst=False,
                         dayfirst=True)
    print(my_dwca.check_dataset())
    sys.exit() 

if stop == 25:
    my_dwca.use_datetime(eventDate='Collection_date',
                         string_to_datetime=True,
                         yearfirst=False,
                         dayfirst=True)
    print(my_dwca.suggest_workflow())
    sys.exit() 

# -----------------------------------------------------------------------------
# use_abundance
# -----------------------------------------------------------------------------
occ = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 
                   'latitude': [-35.310, '-35.273'], 
                   'longitude': [149.125, 149.133], 
                   'date': ['14-01-2023', '15-01-2023'], 
                   'status': ['present', 'present'],
                   'count': [2,1]})

temp_dwca = galaxias.dwca(occurrences=occ,print_notices = False)

if stop == 27:
    temp_dwca.use_abundance(individualCount='count')
    print(temp_dwca.occurrences.head())
    sys.exit() 

# -----------------------------------------------------------------------------
# use_locality
# -----------------------------------------------------------------------------
occ = pd.read_csv('galaxias_user_guide/data/occurrences_dwc.csv')

temp_dwca = galaxias.dwca(occurrences=occ, print_notices = False)

if stop == 29:
    temp_dwca.use_locality(continent='Australia')
    print(temp_dwca.occurrences.head())
    sys.exit() 

if stop == 30:
    temp_dwca.use_locality(continent='Oceania',country='Australia')
    print(temp_dwca.occurrences.head())
    sys.exit() 

# -----------------------------------------------------------------------------
# final
# -----------------------------------------------------------------------------
my_dwca = galaxias.dwca(occurrences = 'galaxias_user_guide/data/occurrences_dwc.csv', print_notices = False)

if stop == 31:
    my_dwca.use_occurrences(basisOfRecord='HumanObservation',occurrenceStatus='PRESENT',occurrenceID=True)
    my_dwca.use_scientific_name(scientificName='Species')
    my_dwca.use_coordinates(decimalLatitude='Latitude',decimalLongitude='Longitude',geodeticDatum='WGS84',coordinatePrecision=0.1)
    my_dwca.use_datetime(eventDate='Collection_date',string_to_datetime=True,yearfirst=False,dayfirst=True)
    my_dwca.check_dataset()
    import sys
    sys.exit()