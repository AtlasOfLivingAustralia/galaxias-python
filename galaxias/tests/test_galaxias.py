import galaxias
import os
import shutil
import pytest
import pandas as pd

# remove data repos for clean testing
if os.path.exists('dwca_data'):
    shutil.rmtree('dwca_data/')

# remove data repos for clean testing
if os.path.exists('dwca_data_occ'):
    shutil.rmtree('dwca_data_occ/')

# remove data repos for clean testing
if os.path.exists('dwca_data_occ_rename'):
    shutil.rmtree('dwca_data_occ_rename/')

# remove data repos for clean testing
if os.path.exists('dwca_data_occ_spec'):
    shutil.rmtree('dwca_data_occ_spec/')

# remove data repos for clean testing
if os.path.exists('dwca_events'):
    shutil.rmtree('dwca_events/')

# remove data repos for clean testing
if os.path.exists('dwca_data_occ_orig'):
    shutil.rmtree('dwca_data_occ_orig/')

# remove data repos for clean testing
if os.path.exists('dwca_data_occ_mm'):
    shutil.rmtree('dwca_data_occ_mm/')

# remove data repos for clean testing
if os.path.exists('dwca_data_occ_emof'):
    shutil.rmtree('dwca_data_occ_emof/')

# remove data repos for clean testing
if os.path.exists('dwca_data_occ_emof_mm'):
    shutil.rmtree('dwca_data_occ_emof_mm/')

# remove data repos for clean testing
if os.path.exists('dwca_data_occ_mm_emof'):
    shutil.rmtree('dwca_data_occ_mm_emof/')
#'''
# -------------------------------------------------------------------------------------------------
# Data Directory Creation
# -------------------------------------------------------------------------------------------------
def test_data_directory_creation_default():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv')
    assert os.path.exists('dwca_data')

def test_data_directory_creation_default_data_raw():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv')
    assert os.path.exists('dwca_data/data_raw')

def test_data_directory_creation_default_data_raw_indir():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv')
    assert os.path.exists('dwca_data/data_raw/occurrences_dwc_clean.csv')

def test_data_directory_creation_default_data_processed():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv')
    assert os.path.exists('dwca_data/data_processed')

def test_data_directory_creation_default_metadata():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv')
    assert os.path.exists('dwca_data/metadata.md')

def test_data_directory_creation_specific():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    assert os.path.exists('dwca_data_occ')

def test_data_directory_creation_specific_data_raw():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    assert os.path.exists('dwca_data_occ/data_raw')

def test_data_directory_creation_specific_data_raw_indir():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    assert os.path.exists('dwca_data_occ/data_raw/occurrences_dwc_clean.csv')

def test_data_directory_creation_specific_data_processed():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    assert os.path.exists('dwca_data_occ/data_processed')

def test_data_directory_creation_specific_metadata():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    assert os.path.exists('dwca_data_occ/metadata.md')

# -------------------------------------------------------------------------------------------------
# use_* function tests
# -------------------------------------------------------------------------------------------------

def use_occurrences():
    n=1

def use_scientific_name():
    n=1

def use_datetime():
    n=1

def use_coordinates():
    n=1


# -------------------------------------------------------------------------------------------------
# metadata function tests
# -------------------------------------------------------------------------------------------------

# def test_make_eml_xml():
#     occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
#     occ_dwca.make_eml_xml()
#     assert os.path.exists(occ_dwca.eml_xml) is True

# def test_make_meta_xml():
#     occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
#     occ_dwca.make_eml_xml()
#     occ_dwca.make_meta_xml()
#     assert os.path.exists(occ_dwca.meta_xml) is True





# def test_add_taxonomic_information():
#     occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename')
#     occ_dwca.add_taxonomic_information()
#     assert set(list(occ_dwca.occurrences.columns)).issuperset(set(["scientificName","vernacularName","genus","family","order","class","phylum","kingdom"]))

# def test_add_unique_occurrence_IDs_default():
#     occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename')
#     occ_dwca.add_unique_occurrence_IDs()
#     assert 'occurrenceID' in list(occ_dwca.occurrences.columns)

# def test_add_unique_occurrence_IDs_specific():
#     occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename')
#     occ_dwca.add_unique_occurrence_IDs(column_name='catalogNumber')
#     assert 'catalogNumber' in list(occ_dwca.occurrences.columns)


'''
# -------------------------------------------------------------------------------------------------
# Check occurrences information
# -------------------------------------------------------------------------------------------------
def test_check_species_names_true():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ_spec')
    test = occ_dwca.check_species_names()
    assert type(test) is bool

def test_check_species_names_true():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ_spec')
    test = occ_dwca.check_species_names()
    assert test is True

def test_check_species_false_type():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename')
    test = occ_dwca.check_species_names()
    assert type(test) is tuple

def test_check_species_false_false():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename')
    test = occ_dwca.check_species_names()
    assert test[0] is False

def test_check_species_false_type_dataframe():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename')
    test = occ_dwca.check_species_names()
    assert type(test[1]) is pd.core.frame.DataFrame

def test_check_species_false_dataframe_empty():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename')
    test = occ_dwca.check_species_names()
    assert not test[1].empty

def test_check_occurrences():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    check_occ = occ_dwca.check_occurrences()
    assert check_occ is True

def test_check_occurrences_wrong_dwc_terms():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrence_data_ORIG.csv',working_dir='dwca_data_occ_orig') 
    with pytest.raises(Exception) as e_info:
        check_occ = occ_dwca.check_occurrences()
    assert str(e_info.value) == "Your column names do not comply with the DwC standard."

# def test_check_occurrences_wrong_dwc_values():
#     occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrence_data_ORIG.csv',working_dir='dwca_data_occ') 
#     with pytest.raises(Exception) as e_info:
#         check_occ = occ_dwca.check_occurrences()
#     assert str(e_info.value) == "The values in some of your columns do not comply with the DwC standard."

def test_check_occurrences_no_occurrence_ids():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename') 
    with pytest.raises(Exception) as e_info:
        check_occ = occ_dwca.check_occurrences()
    assert str(e_info.value) == "You need to add unique identifiers into your occurrences."

def test_check_unique_occurrence_ids():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ_rename')
    occ_dwca.add_unique_occurrence_IDs()
    test = occ_dwca.check_unique_occurrence_ids()
    assert test is True

# -------------------------------------------------------------------------------------------------
# Check events information
# -------------------------------------------------------------------------------------------------
def test_check_events_False():
    events_dwca = galaxias.dwca(events="data_for_testing/events.csv",occurrences="data_for_testing/occurrences_event_multi.csv",working_dir='dwca_events')
    test = events_dwca.check_events()
    assert test is False

def test_check_events_True():
    events_dwca = galaxias.dwca(events="data_for_testing/events.csv",occurrences="data_for_testing/occurrences_event_multi.csv",working_dir='dwca_events')
    temp_events = events_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_dwca.events = temp_events
    test = events_dwca.check_events()
    assert test is True

def test_check_events_duplicate_eventIDs():
    events_dwca = galaxias.dwca(events="data_for_testing/events_duplicate.csv",occurrences="data_for_testing/occurrences_event_multi.csv",working_dir='dwca_events')
    temp_events = events_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_dwca.events = temp_events
    test = events_dwca.check_events()
    assert test is False

# -------------------------------------------------------------------------------------------------
# Check multimedia information
# -------------------------------------------------------------------------------------------------

def test_check_multimedia_occurrences_False():
    occ_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_multi.csv',
                                multimedia='data_for_testing/multimedia_occ_typo.csv',
                                working_dir='dwca_data_occ_mm')
    with pytest.raises(Exception) as e_info:
        check_occ = occ_mm_dwca.check_occurrences()
    assert str(e_info.value) == "Your column names do not comply with the DwC standard."
    

def test_check_multimedia_occurrences_True():
    occ_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_multi.csv',
                                multimedia='data_for_testing/multimedia_occ.csv',
                                working_dir='dwca_data_occ_mm')
    test = occ_mm_dwca.check_multimedia()
    assert test is True

def test_check_multimedia_events_False():
    occ_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                events='data_for_testing/events.csv',
                                multimedia='data_for_testing/multimedia_event_typo.csv',
                                working_dir='dwca_data_occ_mm')
    with pytest.raises(Exception) as e_info:
        check_occ = occ_mm_dwca.check_occurrences()
    assert str(e_info.value) == "Your column names do not comply with the DwC standard."
    

def test_check_multimedia_events_True():
    occ_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                events='data_for_testing/events.csv',
                                multimedia='data_for_testing/multimedia_event.csv',
                                working_dir='dwca_data_occ_mm')
    test = occ_mm_dwca.check_multimedia()
    assert test is True

# -------------------------------------------------------------------------------------------------
# Check emof information
# -------------------------------------------------------------------------------------------------

def test_check_emof_False():
    occ_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                events='data_for_testing/events.csv',
                                multimedia='data_for_testing/multimedia_event.csv',
                                emof='data_for_testing/extendedMeasurementOrFact.csv',
                                working_dir='dwca_data_occ_emof_mm')
    with pytest.raises(Exception) as e_info:
        check_occ = occ_mm_dwca.check_emof()
    message = str(e_info.value)
    assert "Your column names do not comply with the DwC standard" in message
    

def test_check_emof_events_True():
    occ_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                events='data_for_testing/events.csv',
                                multimedia='data_for_testing/multimedia_event.csv',
                                emof='data_for_testing/extendedMeasurementOrFact.csv',
                                working_dir='dwca_data_occ_emof_mm')
    temp_emof = occ_mm_dwca.emof.rename(columns={"measurement": "measurementType",
                                            "value": "measurementValue",
                                            "unit": "measurementUnit",
                                            "error": "measurementAccuracy"})
    occ_mm_dwca.emof = temp_emof
    test = occ_mm_dwca.check_emof()
    assert test is True

# -------------------------------------------------------------------------------------------------
# Check xml information
# -------------------------------------------------------------------------------------------------
def test_check_xml_information():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    occ_dwca.make_eml_xml()
    test = occ_dwca.check_xmls()
    assert test is None

# -------------------------------------------------------------------------------------------------
# Check checking dwca information
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# Check creating dwca information
# -------------------------------------------------------------------------------------------------


def test_create_dwca_occurrence_default():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    occ_dwca.make_eml_xml()
    occ_dwca.make_meta_xml()
    occ_dwca.create_dwca()
    assert os.path.exists(occ_dwca.dwca_name) is True

def test_create_dwca_occurrence_specific_name():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    occ_dwca.make_eml_xml()
    occ_dwca.make_meta_xml()
    occ_dwca.dwca_name = 'my_dwca.zip'
    occ_dwca.create_dwca()
    assert os.path.exists(occ_dwca.dwca_name) is True

def test_create_dwca_occurrence_mm_default():
    occ_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrence_dwc_multi_clean.csv',
                                multimedia='data_for_testing/multimedia_occ.csv',
                                working_dir='dwca_data_occ_mm')
    occ_mm_dwca.make_eml_xml()
    occ_mm_dwca.make_meta_xml()
    occ_mm_dwca.create_dwca()
    assert os.path.exists(occ_mm_dwca.dwca_name) is True

def test_create_dwca_occurrence_mm_specific_name():
    occ_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrence_dwc_multi_clean.csv',
                                multimedia='data_for_testing/multimedia_occ.csv',
                                working_dir='dwca_data_occ_mm')
    occ_mm_dwca.make_eml_xml()
    occ_mm_dwca.make_meta_xml()
    occ_mm_dwca.dwca_name = 'my_dwca.zip'
    occ_mm_dwca.create_dwca()
    assert os.path.exists(occ_mm_dwca.dwca_name) is True

def test_create_dwca_event_default():
    events_dwca = galaxias.dwca(events="data_for_testing/events.csv",occurrences="data_for_testing/occurrences_event_multi.csv",working_dir='dwca_events')
    temp_events = events_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_dwca.events = temp_events
    temp_occurrences = events_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
    events_dwca.occurrences = temp_occurrences
    events_dwca.add_taxonomic_information()
    events_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    events_dwca.occurrences["geodeticDatum"] = "WGS84"
    events_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    events_dwca.make_eml_xml()
    events_dwca.make_meta_xml()
    events_dwca.create_dwca()
    assert os.path.exists(events_dwca.dwca_name) is True

def test_create_dwca_event_specific_name():
    events_dwca = galaxias.dwca(events="data_for_testing/events.csv",occurrences="data_for_testing/occurrences_event_multi.csv",working_dir='dwca_events')
    temp_events = events_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_dwca.events = temp_events
    temp_occurrences = events_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
    events_dwca.occurrences = temp_occurrences
    events_dwca.add_taxonomic_information()
    events_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    events_dwca.occurrences["geodeticDatum"] = "WGS84"
    events_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    events_dwca.make_eml_xml()
    events_dwca.make_meta_xml()
    events_dwca.dwca_name = 'my_dwca.zip'
    events_dwca.create_dwca()
    assert os.path.exists(events_dwca.dwca_name) is True

def test_create_dwca_event_mm_default():
    events_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                events='data_for_testing/events.csv',
                                multimedia='data_for_testing/multimedia_event.csv',
                                working_dir='dwca_data_occ_mm')
    temp_events = events_mm_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_mm_dwca.events = temp_events
    temp_occurrences = events_mm_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
    events_mm_dwca.occurrences = temp_occurrences
    events_mm_dwca.add_taxonomic_information()
    events_mm_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    events_mm_dwca.occurrences["geodeticDatum"] = "WGS84"
    events_mm_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    events_mm_dwca.make_eml_xml()
    events_mm_dwca.make_meta_xml()
    events_mm_dwca.create_dwca()
    assert os.path.exists(events_mm_dwca.dwca_name) is True

def test_create_dwca_event_mm_specific_name():
    events_mm_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                events='data_for_testing/events.csv',
                                multimedia='data_for_testing/multimedia_event.csv',
                                working_dir='dwca_data_occ_mm')
    temp_events = events_mm_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_mm_dwca.events = temp_events
    temp_occurrences = events_mm_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
    events_mm_dwca.occurrences = temp_occurrences
    events_mm_dwca.add_taxonomic_information()
    events_mm_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    events_mm_dwca.occurrences["geodeticDatum"] = "WGS84"
    events_mm_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    events_mm_dwca.make_eml_xml()
    events_mm_dwca.make_meta_xml()
    events_mm_dwca.dwca_name = 'my_dwca.zip'
    events_mm_dwca.create_dwca()
    assert os.path.exists(events_mm_dwca.dwca_name) is True
#'''
'''
def test_create_dwca_event_emof_default():
    events_emof_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                  events='data_for_testing/events.csv',
                                  emof='data_for_testing/extendedMeasurementOrFact.csv',
                                  working_dir='dwca_data_occ_emof')
    temp_events = events_emof_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_emof_dwca.events = temp_events
    temp_occurrences = events_emof_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
    events_emof_dwca.occurrences = temp_occurrences
    events_emof_dwca.add_taxonomic_information()
    events_emof_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    events_emof_dwca.occurrences["geodeticDatum"] = "WGS84"
    events_emof_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    temp_emof = events_emof_dwca.emof.rename(columns={"measurement": "measurementType",
                                            "value": "measurementValue",
                                            "unit": "measurementUnit",
                                            "error": "measurementAccuracy"})
    events_emof_dwca.emof = temp_emof
    events_emof_dwca.make_eml_xml()
    events_emof_dwca.make_meta_xml()
    events_emof_dwca.create_dwca()
    assert os.path.exists(events_emof_dwca.dwca_name) is True

def test_create_dwca_event_emof_specific_name():
    events_emof_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                  events='data_for_testing/events.csv',
                                  emof='data_for_testing/extendedMeasurementOrFact.csv',
                                  working_dir='dwca_data_occ_emof')
    temp_events = events_emof_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_emof_dwca.events = temp_events
    temp_occurrences = events_emof_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
    events_emof_dwca.occurrences = temp_occurrences
    events_emof_dwca.add_taxonomic_information()
    events_emof_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    events_emof_dwca.occurrences["geodeticDatum"] = "WGS84"
    events_emof_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    temp_emof = events_emof_dwca.emof.rename(columns={"measurement": "measurementType",
                                            "value": "measurementValue",
                                            "unit": "measurementUnit",
                                            "error": "measurementAccuracy"})
    events_emof_dwca.emof = temp_emof
    events_emof_dwca.make_eml_xml()
    events_emof_dwca.make_meta_xml()
    events_emof_dwca.dwca_name = 'my_dwca.zip'
    events_emof_dwca.create_dwca()
    assert os.path.exists(events_emof_dwca.dwca_name) is True

def test_create_dwca_event_mm_emof_default():
    events_emof_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                  events='data_for_testing/events.csv',
                                  emof='data_for_testing/extendedMeasurementOrFact.csv',
                                  multimedia='data_for_testing/multimedia_event.csv',
                                  working_dir='dwca_data_occ_mm_emof')
    temp_events = events_emof_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_emof_dwca.events = temp_events
    temp_occurrences = events_emof_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
    events_emof_dwca.occurrences = temp_occurrences
    events_emof_dwca.add_taxonomic_information()
    events_emof_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    events_emof_dwca.occurrences["geodeticDatum"] = "WGS84"
    events_emof_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    temp_emof = events_emof_dwca.emof.rename(columns={"measurement": "measurementType",
                                            "value": "measurementValue",
                                            "unit": "measurementUnit",
                                            "error": "measurementAccuracy"})
    events_emof_dwca.emof = temp_emof
    events_emof_dwca.make_eml_xml()
    events_emof_dwca.make_meta_xml()
    events_emof_dwca.create_dwca()
    assert os.path.exists(events_emof_dwca.dwca_name) is True

def test_create_dwca_event_mm_emof_specific_name():
    events_emof_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_event_multi.csv',
                                  events='data_for_testing/events.csv',
                                  emof='data_for_testing/extendedMeasurementOrFact.csv',
                                  multimedia='data_for_testing/multimedia_event.csv',
                                  working_dir='dwca_data_occ_mm_emof')
    temp_events = events_emof_dwca.events.rename(columns = {"eventName": "Event"})
    temp_events['samplingProtocol'] = "observation"
    events_emof_dwca.events = temp_events
    temp_occurrences = events_emof_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
    events_emof_dwca.occurrences = temp_occurrences
    events_emof_dwca.add_taxonomic_information()
    events_emof_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
    events_emof_dwca.occurrences["geodeticDatum"] = "WGS84"
    events_emof_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
    temp_emof = events_emof_dwca.emof.rename(columns={"measurement": "measurementType",
                                            "value": "measurementValue",
                                            "unit": "measurementUnit",
                                            "error": "measurementAccuracy"})
    events_emof_dwca.emof = temp_emof
    events_emof_dwca.make_eml_xml()
    events_emof_dwca.make_meta_xml()
    events_emof_dwca.dwca_name = 'my_dwca.zip'
    events_emof_dwca.create_dwca()
    assert os.path.exists(events_emof_dwca.dwca_name) is True
'''