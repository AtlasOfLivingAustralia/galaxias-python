import galaxias
import pandas as pd
import sys
import datetime

# get option
stopping_point = sys.argv[1]

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# --------------------------------------------------------
# Part 1: Read In Data
# --------------------------------------------------------
# read in data
my_dwca = galaxias.dwca(occurrences="galaxias_user_guide/occurrences_dwc.csv")

if stopping_point == "1":
    my_dwca.check_data() #print()
    sys.exit()

# --------------------------------------------------------
# Part 2: use_occurrences()
# --------------------------------------------------------

my_dwca.use_occurrences(occurrenceID = True)

if stopping_point == "2":
    print(my_dwca.occurrences.head())
    sys.exit()

my_dwca.use_occurrences(basisOfRecord = "HumanObservation")
# my_dwca.occurrences['basisOfRecord'] = "HumaObservation"

if stopping_point == "3":
    print(my_dwca.occurrences.head())
    sys.exit()

if stopping_point == "4":
    my_dwca.check_data() #print()
    sys.exit()

# --------------------------------------------------------
# Part 3: use_scientific_name()
# --------------------------------------------------------

my_dwca.use_scientific_name(scientific_name = my_dwca.occurrences['Species'])

if stopping_point == "5":
    print(my_dwca.occurrences.head())
    sys.exit()

if stopping_point == "6":
    my_dwca.check_data() #print()
    sys.exit()

# --------------------------------------------------------
# Part 4: use_coordinates()
# --------------------------------------------------------

# my_dwca.use_coordinates()

my_dwca.use_coordinates(decimalLatitude=my_dwca.occurrences['Latitude'],
                        decimalLongitude=my_dwca.occurrences['Longitude'])

if stopping_point == "7":
    print(my_dwca.occurrences.head())
    sys.exit()

my_dwca.use_coordinates(geodeticDatum='WGS84',
                        coordinateUncertaintyInMeters=100,
                        coordinatePrecision=0.01)

if stopping_point == "8":
    print(my_dwca.occurrences.head())
    sys.exit()

if stopping_point == "9":
    my_dwca.check_data()
    sys.exit()

# --------------------------------------------------------
# Part 5: use_datetime()
# --------------------------------------------------------

if stopping_point == "10":
    print(my_dwca.occurrences.head())
    sys.exit()

if stopping_point == "11":
    my_dwca.use_datetime(eventDate=my_dwca.occurrences['Collection_date'])

my_dwca.use_datetime(eventDate=my_dwca.occurrences['Collection_date'],
                     string_to_datetime=True,
                     orig_format='%d/%m/%Y')

if stopping_point == "12":
    print(my_dwca.occurrences.head())
    sys.exit()

if stopping_point == "13":
    my_dwca.check_data()
    sys.exit()
# --------------------------------------------------------
# Part 6: use_locality() (OPTIONAL)
# --------------------------------------------------------

# --------------------------------------------------------
# Part 7: write out data
# --------------------------------------------------------

if stopping_point == "99":
    my_dwca.check_data() #print()
    sys.exit()

my_dwca.occurrences.to_csv("galaxias_user_guide/occurrences_dwc_clean.csv",index=False)
# sys.exit()


# --------------------------------------------------------

'''
if "check_taxon" in stopping_point or stopping_point == "add_taxon":

    if stopping_point == "check_taxon1":
        print(my_dwca.generate_data_report())
        sys.exit()

    name_changes = {
        "Eucalyptus camaldulensis var. obtusa": "Eucalyptus camaldulensis subsp. obtusa",
        "Acacia murayana": "Acacia murrayana",
        "Eucalyptus sclerophylla": "Eucalyptus racemosa"
    }
    for name in name_changes:
        my_dwca.occurrences['scientificName'] = my_dwca.occurrences['scientificName'].replace(regex=name, value=name_changes[name])

    if stopping_point == "check_taxon":
        print(my_dwca.occurrences)
        sys.exit()

if stopping_point == "add_taxon":
    my_dwca.add_taxonomic_information()
    print(my_dwca.occurrences.head())
    sys.exit()

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

    # add higher taxon
    my_dwca.add_taxonomic_information()

    # add required columns
    my_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    my_dwca.occurrences["geodeticDatum"] = "WGS84"
    my_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"

    # add occurrence IDs
    my_dwca.add_unique_occurrence_IDs(column_name="occurrenceID")

    

    ### TODO: add this step
    temp_occurrences = my_dwca.occurrences.rename(
        columns = {
            "classs": "class",
        }
    )
    my_dwca.occurrences = temp_occurrences

    for i,row in my_dwca.occurrences.iterrows():
        split_date = list(map(int, row["eventDate"].split("/")))
        my_dwca.occurrences.at[i,"eventDate"] = str(datetime.date(split_date[2],split_date[1],split_date[0]))
'''
