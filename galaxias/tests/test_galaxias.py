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

def test_use_occurrences_catch_error():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    with pytest.raises(Exception) as e_info:
        occ_dwca.use_occurrences()
    assert "No Darwin Core" in str(e_info.value)
    
def test_use_occurrences_add_bor_correct():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    temp = occ_dwca.use_occurrences(basisOfRecord='HumanObservation')
    assert temp is None

def test_use_occurrences_add_bor_incorrect():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_clean.csv',working_dir='dwca_data_occ')
    with pytest.raises(Exception) as e_info:
        occ_dwca.use_occurrences(basisOfRecord='HumaObservation')
    assert "There are invalid basisOfRecord values." in str(e_info.value)

def test_use_occurrences_rename_bor():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ')
    occ_dwca.occurrences['bor'] = 'HumanObservation'
    temp = occ_dwca.use_occurrences(basisOfRecord=occ_dwca.occurrences['bor'])
    assert temp is None

def test_use_occurrences_rename_occID():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ')
    occ_dwca.occurrences['id'] = [i for i in range(occ_dwca.occurrences.shape[0])]
    temp = occ_dwca.use_occurrences(occurrenceID = occ_dwca.occurrences['id'])
    assert temp is None

def test_use_occurrences_create_unique_ids():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc.csv',working_dir='dwca_data_occ')
    temp = occ_dwca.use_occurrences(occurrenceID = True)
    assert temp is None

def test_use_scientific_name_rename():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc.csv',working_dir='dwca_data_occ')
    temp = occ_dwca.use_scientific_name(scientific_name=occ_dwca.occurrences['Species'])
    assert temp is None

def test_use_datetime_format_error():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc.csv',working_dir='dwca_data_occ')
    with pytest.raises(Exception) as e_info:
        occ_dwca.use_datetime(eventDate=occ_dwca.occurrences['Collection_date'])
    assert "Data is not in datetime format" in str(e_info.value)

def test_use_datetime_string_to_datetime():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc.csv',working_dir='dwca_data_occ')
    temp = occ_dwca.use_datetime(eventDate=occ_dwca.occurrences['Collection_date'],
                                 string_to_datetime=True,
                                 orig_format='%d/%m/%Y')
    assert temp is None

def test_use_coordinates():
    occ_dwca = galaxias.dwca(occurrences='data_for_testing/occurrences_dwc.csv',working_dir='dwca_data_occ')
    temp = occ_dwca.use_coordinates(decimalLatitude=occ_dwca.occurrences['Latitude'],
                                    decimalLongitude=occ_dwca.occurrences['Longitude'])
    assert temp is None

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

# -------------------------------------------------------------------------------------------------
# Check events information
# -------------------------------------------------------------------------------------------------
'''
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