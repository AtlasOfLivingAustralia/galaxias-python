import galaxias
import os
import shutil
import pandas as pd
import pytest

def test_check_schema_occurrences():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    build_occurrences()
    galaxias.use_schema()
    result = galaxias.check_schema()
    assert result is True
#'''
def test_check_schema_occurrences_rename():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    build_occurrences()
    galaxias.use_schema(schema='test.xml')
    result = galaxias.check_schema(schema='test.xml')
    assert result is True

def test_check_schema_no_schema():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    build_occurrences()
    with pytest.raises(Exception) as e_info:
        result = galaxias.check_schema()
    assert "schema" in str(e_info.value)

def test_check_schema_events():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    build_events()
    # now write schema
    galaxias.use_schema()
    result = galaxias.check_schema()
    assert result is True

def test_check_schema_events_rename():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    build_events()
    # now write schema
    galaxias.use_schema(schema='test.xml')
    result = galaxias.check_schema(schema='test.xml')
    assert result is True
#'''
def build_occurrences():
    # get occurrences columns ready
    occurrences = pd.read_csv('../../docs/source/galaxias_user_guide/data/dummy-dataset-sb.csv')
    occurrences.columns = map(str.lower, occurrences.columns)

    # set all of the data to Darwin Core titles
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

    # only choose Darwin Core compliant terms
    occ_terms = list(galaxias.occurrence_terms())
    occ_terms_dwca = list(set(occ_terms).intersection(list(occurrences.columns)))
    occurrences_final = occurrences[occ_terms_dwca]

    # write out the data
    galaxias.use_data(occurrences=occurrences_final)

    # get metadata
    galaxias.use_metadata_template()
    galaxias.use_metadata()

def build_events():
    # get data
    sites = pd.read_csv('../../docs/source/galaxias_user_guide/data/sites.csv')
    observations = pd.read_csv('../../docs/source/galaxias_user_guide/data/observations.csv')
    species = pd.read_csv('../../docs/source/galaxias_user_guide/data/species_list.csv')

    # get list of all species abbreviations 
    species_abb = list(species['abbreviation'])

    # join observations and select sites columns by site_code
    observations_site = observations[['site_code','year'] + species_abb]

    # add eventID to dataframe
    observations_site_id = galaxias.set_events(dataframe=observations_site,eventID=['sequential','site_code','year'])

    # coords
    observations_site_id_coords = observations_site_id.merge(sites[['site_code','latitude','longitude']],on='site_code',how='left')
    events_all = galaxias.set_coordinates(dataframe=observations_site_id_coords,
                                          decimalLatitude='latitude',
                                          decimalLongitude='longitude',
                                          coordinateUncertaintyInMeters = 30,
                                          geodeticDatum = 'WGS84')

    # event terms
    event_terms = list(galaxias.event_terms())
    event_terms_dwca = list(set(event_terms).intersection(list(events_all.columns)))
    events = events_all[event_terms_dwca]

    # melting the pandas dataframe to make it more occurrences-like
    observations_site_id_select = observations_site_id[['eventID'] + species_abb]
    observations_site_id_abbr = observations_site_id_select.melt(id_vars=['eventID'],
                                                                 var_name='abbreviation',
                                                                 value_name='status')

    observations_site_id_spec = observations_site_id_abbr.merge(species,on='abbreviation',how='left')

    # first, change the 1's and 0's to PRESENT and ABSENT
    observations_site_id_spec['status'] = observations_site_id_spec['status'].map({1: 'PRESENT', 0: 'ABSENT'})

    # now, we will reformat the data to use valid Darwin Core columns
    obs = galaxias.set_occurrences(occurrences=observations_site_id_spec,
                                occurrenceID=['eventID','sequential'],
                                basisOfRecord = 'HumanObservation',
                                occurrenceStatus = 'status')
    obs_name = galaxias.set_scientific_name(dataframe=obs,scientificName='scientific_name')
    obs_dwc = galaxias.set_taxonomy(dataframe=obs_name,vernacularName='common_name')

    # get occurrences
    occ_terms = list(galaxias.occurrence_terms())
    occ_terms_dwca = list(set(occ_terms).intersection(list(obs_dwc.columns)))
    occurrences = obs_dwc[occ_terms_dwca]

    # write out data
    galaxias.use_data(occurrences=occurrences,events=events)

    # get metadata
    galaxias.use_metadata_template()
    galaxias.use_metadata()