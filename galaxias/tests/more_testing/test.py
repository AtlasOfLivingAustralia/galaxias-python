import galaxias    
import os
import pandas as pd

df = pd.DataFrame(
    {
        "latitude": [-35.310, "-35.273"], # deliberate error for demonstration purposes
        "longitude": [149.125, 149.133],
        "date": ["14-01-2023", "15-01-2023"],
        "date2": ["14-01-2023 10:23:00", "14-01-2023 10:24:01"],
        "time": ["10:23", "11:25"],
        "time2": ["10:23:00", "11:25:00"],
        "month": ["Jan", "BLF"],
        "month2": ["January", "February"],
        "day": [100, 101],
        "day2": ["100", "101"],
        "species": ["Callocephalon fimbriatum", "Eolophus roseicapilla"],
        "n": [2, 3],
        "crs": ["WGS84", "WGS8d"],
        "country1": ["AU", "DE"],
        "country_real": ["Naustralia", "Denmark"],
        "continent": ["bork", "Europe"]
})
occ_dwca = galaxias.dwca(occurrences=df,working_dir='dwca_data_occ')
# occ_dwca.check_data()
occ_dwca.use_occurrences(basisOfRecord = "HumanObservation")
occ_dwca.use_occurrences(occurrenceID = True)
occ_dwca.use_scientific_name(scientific_name = occ_dwca.occurrences['species'])
# occ_dwca.use_coordinates(decimalLatitude=occ_dwca.occurrences['latitude'],
#                          decimalLongitude=occ_dwca.occurrences['longitude'],
#                          geodeticDatum='WGS84',
#                          coordinateUncertaintyInMeters=100,
#                          coordinatePrecision=0.01)
occ_dwca.use_datetime()
occ_dwca.check_data()

# if os.path.exists('dwca_data_occ'):
#     os.rmdir('dwca_data_occ')
# occ_dwca = galaxias.dwca(occurrences='../data_for_testing/occurrences_dwc_rename.csv',working_dir='dwca_data_occ')
# occ_dwca.make_eml_xml()
# occ_dwca.make_meta_xml()
# occ_dwca.create_dwca()
# occ_dwca.check_data()

# if os.path.exists('dwca_data_occ_mm'):
#     os.rmdir('dwca_data_occ_mm')
# occ_mm_dwca = galaxias.dwca(occurrences='../data_for_testing/occurrence_dwc_multi_clean.csv',
#                             multimedia='../data_for_testing/multimedia_occ.csv',
#                             working_dir='dwca_data_occ_mm')
# occ_mm_dwca.make_eml_xml()
# occ_mm_dwca.make_meta_xml()
# occ_mm_dwca.create_dwca()
# # occ_mm_dwca.generate_archive_report()

# if os.path.exists('dwca_events'):
#     os.rmdir('dwca_events')
# events_dwca = galaxias.dwca(events="../data_for_testing/events.csv",
#                             occurrences="../data_for_testing/occurrences_event_multi.csv",
#                             working_dir='dwca_events')
# temp_events = events_dwca.events.rename(columns = {"eventName": "Event"})
# temp_events['samplingProtocol'] = "observation"
# events_dwca.events = temp_events
# temp_occurrences = events_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
# events_dwca.occurrences = temp_occurrences
# events_dwca.add_taxonomic_information()
# events_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
# events_dwca.occurrences["geodeticDatum"] = "WGS84"
# events_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
# events_dwca.make_eml_xml()
# events_dwca.make_meta_xml()
# events_dwca.create_dwca()

# if os.path.exists('dwca_events_occ_mm'):
#     os.rmdir('dwca_events_occ_mm')
# events_mm_dwca = galaxias.dwca(occurrences='../data_for_testing/occurrences_event_multi.csv',
#                             events='../data_for_testing/events.csv',
#                             multimedia='../data_for_testing/multimedia_event.csv',
#                             working_dir='dwca_events_occ_mm')
# temp_events = events_mm_dwca.events.rename(columns = {"eventName": "Event"})
# temp_events['samplingProtocol'] = "observation"
# events_mm_dwca.events = temp_events
# temp_occurrences = events_mm_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
# events_mm_dwca.occurrences = temp_occurrences
# events_mm_dwca.add_taxonomic_information()
# events_mm_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
# events_mm_dwca.occurrences["geodeticDatum"] = "WGS84"
# events_mm_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
# events_mm_dwca.make_eml_xml()
# events_mm_dwca.make_meta_xml()
# events_mm_dwca.create_dwca()

# if os.path.exists('dwca_events_occ_mm_emof'):
#     os.rmdir('dwca_devents_occ_mm_emof')
# events_emof_dwca = galaxias.dwca(occurrences='../data_for_testing/occurrences_event_multi.csv',
#                                 events='../data_for_testing/events.csv',
#                                 emof='../data_for_testing/extendedMeasurementOrFact.csv',
#                                 multimedia='../data_for_testing/multimedia_event.csv',
#                                 working_dir='dwca_events_occ_mm_emof')
# temp_events = events_emof_dwca.events.rename(columns = {"eventName": "Event"})
# temp_events['samplingProtocol'] = "observation"
# events_emof_dwca.events = temp_events
# temp_occurrences = events_emof_dwca.occurrences.rename(columns = {"Species": "scientificName","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Collection_date": "eventDate","number_birds": "individualCount"})
# events_emof_dwca.occurrences = temp_occurrences
# events_emof_dwca.add_taxonomic_information()
# events_emof_dwca.occurrences["coordinateUncertaintyInMeters"] = 100
# events_emof_dwca.occurrences["geodeticDatum"] = "WGS84"
# events_emof_dwca.occurrences["basisOfRecord"] = "HUMAN_OBSERVATION"
# temp_emof = events_emof_dwca.emof.rename(columns={"measurement": "measurementType",
#                                         "value": "measurementValue",
#                                         "unit": "measurementUnit",
#                                         "error": "measurementAccuracy"})
# events_emof_dwca.emof = temp_emof
# events_emof_dwca.make_eml_xml()
# events_emof_dwca.make_meta_xml()
# events_emof_dwca.create_dwca()
