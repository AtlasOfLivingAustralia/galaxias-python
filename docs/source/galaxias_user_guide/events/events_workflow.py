import galaxias
import pandas as pd
import sys

# get option
stop = int(sys.argv[1])

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# --------------------------------------------------------
# Initialising and suggesting workflow
# --------------------------------------------------------
sites = pd.read_csv('galaxias_user_guide/data/sites.csv')

if stop == 1:
    print(sites)
    sys.exit()

observations = pd.read_csv('galaxias_user_guide/data/observations.csv')

if stop == 2:
    print(observations)
    sys.exit()

species = pd.read_csv('galaxias_user_guide/data/species_list.csv')

if stop == 3:
    print(species)
    sys.exit()

# get list of all species abbreviations 
species_abb = list(species['abbreviation'])

# join observations and select sites columns by site_code
observations_site = observations[['site_code','year'] + species_abb]

# add eventID to dataframe
observations_site_id = galaxias.set_events(dataframe=observations_site,eventID=['sequential','site_code','year'])

if stop == 4:
    print(observations_site_id)
    sys.exit()

observations_site_id_coords = observations_site_id.merge(sites[['site_code','latitude','longitude']],on='site_code',how='left')
events_all = galaxias.set_coordinates(dataframe=observations_site_id_coords,
                                                         decimalLatitude='latitude',
                                                         decimalLongitude='longitude',
                                                         coordinateUncertaintyInMeters = 30,
                                                         geodeticDatum = 'WGS84')

if stop == 5:
    print(events_all)
    sys.exit()


event_terms = list(galaxias.event_terms())
event_terms_dwca = list(set(event_terms).intersection(list(events_all.columns)))
events = events_all[event_terms_dwca]
events

if stop == 6:
    print(events)
    sys.exit()

observations_site_id_select = observations_site_id[['eventID'] + species_abb]
observations_site_id_abbr = observations_site_id_select.melt(id_vars=['eventID'],
                                                             var_name='abbreviation',
                                                             value_name='status')

if stop == 7:
    print(observations_site_id_abbr)
    sys.exit()

observations_site_id_spec = observations_site_id_abbr.merge(species,on='abbreviation',how='left')

if stop == 8:
    print(observations_site_id_spec)
    sys.exit()

# first, change the 1's and 0's to PRESENT and ABSENT
observations_site_id_spec['status'] = observations_site_id_spec['status'].map({1: 'PRESENT', 0: 'ABSENT'})

# now, we will reformat the data to use valid Darwin Core columns
obs = galaxias.set_occurrences(occurrences=observations_site_id_spec,
                               occurrenceID=['eventID','sequential'],
                               basisOfRecord = 'HumanObservation',
                               occurrenceStatus = 'status')
obs_name = galaxias.set_scientific_name(dataframe=obs,scientificName='scientific_name')
obs_dwc = galaxias.set_taxonomy(dataframe=obs_name,vernacularName='common_name')

if stop == 9:
    print(obs_dwc)
    sys.exit()

occ_terms = list(galaxias.occurrence_terms())
occ_terms_dwca = list(set(occ_terms).intersection(list(obs_dwc.columns)))
occurrences = obs_dwc[occ_terms_dwca]

if stop == 10:
    print(occurrences)
    sys.exit()