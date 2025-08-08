import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_occurrences()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_occurrences_no_arguments():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_occurrences()
    assert "No Darwin Core" in str(e_info.value)

def test_set_occurrences_occurrenceID_rename():
    df = pd.DataFrame({'id': ['1','2']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceID='id')
    assert 'occurrenceID' in list(occ_dwca.occurrences.columns)

#'''
def test_set_occurrences_catalogNumber_rename():
    df = pd.DataFrame({'id': ['1','2']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(catalogNumber='id')
    assert 'catalogNumber' in list(occ_dwca.occurrences.columns)

def test_set_occurrences_recordNumber_rename():
    df = pd.DataFrame({'id': ['1','2']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(recordNumber='id')
    assert 'recordNumber' in list(occ_dwca.occurrences.columns)

def test_set_occurrences_occurrenceID_rename():
    df = pd.DataFrame({'bor': ['HumanObservation','HumanObservation']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(basisOfRecord='bor')
    assert 'basisOfRecord' in list(occ_dwca.occurrences.columns)

def test_set_occurrences_occurrenceStatus_rename():
    df = pd.DataFrame({'status': ['PRESENT','PRESENT']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceStatus='status')
    assert 'occurrenceStatus' in occ_dwca.occurrences.columns

def test_set_occurrences_basisOfRecord_value_incorrect():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'basisOfRecord': ['observation','observation']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_occurrences()
    assert 'basisOfRecord' in str(e_info.value)

def test_set_occurrences_basisOfRecord_value_incorrect_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'bor': ['observation','observation']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_occurrences(basisOfRecord='bor')
    assert 'basisOfRecord' in str(e_info.value)

def test_set_occurrences_occurrenceIDs_value_duplicate():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'occurrenceID': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_occurrences()
    assert 'occurrenceID' in str(e_info.value)

def test_set_occurrences_occurrenceIDs_value_duplicate_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'id': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_occurrences(occurrenceID='id')
    assert 'occurrenceID' in str(e_info.value)

def test_set_occurrences_occurrenceStatus_wrong_value():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'occurrenceStatus': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_occurrences()
    assert 'occurrenceStatus' in str(e_info.value)

def test_set_occurrences_occurrenceStatus__wrong_value_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'status': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_occurrences(occurrenceStatus='status')
    assert 'occurrenceStatus' in str(e_info.value)

# ADD ID STUFF
def test_set_occurrences_add_occurrenceIDs_random():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceID='random')
    assert 'occurrenceID' in occ_dwca.occurrences.columns

def test_set_occurrences_add_occurrenceIDs_sequential():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceID='sequential')
    assert 'occurrenceID' in occ_dwca.occurrences.columns

def test_set_occurrences_add_occurrenceIDs_composite():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceID=['eventDate','catalogNumber'])
    assert 'occurrenceID' in occ_dwca.occurrences.columns

def test_set_occurrences_add_occurrenceIDs_composite_random():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceID=['random','eventDate','catalogNumber'])
    assert 'occurrenceID' in occ_dwca.occurrences.columns

def test_set_occurrences_add_occurrenceIDs_composite_random_last():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceID=['eventDate','catalogNumber','random'])
    assert 'occurrenceID' in occ_dwca.occurrences.columns

def test_set_occurrences_add_occurrenceIDs_composite_sequential():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceID=['sequential','eventDate','catalogNumber'])
    assert 'occurrenceID' in occ_dwca.occurrences.columns

def test_set_occurrences_add_occurrenceIDs_composite_sequential_last():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_occurrences(occurrenceID=['eventDate','catalogNumber','sequential'])
    assert 'occurrenceID' in occ_dwca.occurrences.columns
#'''
