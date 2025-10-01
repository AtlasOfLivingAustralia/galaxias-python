import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        galaxias.set_occurrences()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_occurrences_no_arguments():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_occurrences(occurrences=df)
    assert "No Darwin Core" in str(e_info.value)

def test_set_occurrences_occurrenceID_rename():
    df = pd.DataFrame({'id': ['1','2']})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceID='id')
    assert 'occurrenceID' in list(new_df.columns)

def test_set_occurrences_catalogNumber_rename():
    df = pd.DataFrame({'id': ['1','2']})
    new_df = galaxias.set_occurrences(occurrences=df,catalogNumber='id')
    assert 'catalogNumber' in list(new_df.columns)

def test_set_occurrences_recordNumber_rename():
    df = pd.DataFrame({'id': ['1','2']})
    new_df = galaxias.set_occurrences(occurrences=df,recordNumber='id')
    assert 'recordNumber' in list(new_df.columns)

def test_set_occurrences_occurrenceID_rename():
    df = pd.DataFrame({'bor': ['HumanObservation','HumanObservation']})
    new_df = galaxias.set_occurrences(occurrences=df,basisOfRecord='bor')
    assert 'basisOfRecord' in list(new_df.columns)

def test_set_occurrences_occurrenceStatus_rename():
    df = pd.DataFrame({'status': ['PRESENT','PRESENT']})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceStatus='status')
    assert 'occurrenceStatus' in new_df.columns

def test_set_occurrences_basisOfRecord_value_incorrect():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'basisOfRecord': ['observation','observation']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_occurrences(occurrences=df)
    assert 'basisOfRecord' in str(e_info.value)

def test_set_occurrences_basisOfRecord_value_incorrect_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'bor': ['observation','observation']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_occurrences(occurrences=df,basisOfRecord='bor')
    assert 'basisOfRecord' in str(e_info.value)

def test_set_occurrences_occurrenceIDs_value_duplicate():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'occurrenceID': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_occurrences(occurrences=df)
    assert 'occurrenceID' in str(e_info.value)

def test_set_occurrences_occurrenceIDs_value_duplicate_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'id': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_occurrences(occurrences=df,occurrenceID='id')
    assert 'occurrenceID' in str(e_info.value)

def test_set_occurrences_occurrenceStatus_wrong_value():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'occurrenceStatus': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_occurrences(occurrences=df)
    assert 'occurrenceStatus' in str(e_info.value)

def test_set_occurrences_occurrenceStatus__wrong_value_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0],
                       'status': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_occurrences(occurrences=df,occurrenceStatus='status')
    assert 'occurrenceStatus' in str(e_info.value)

# ADD ID STUFF
def test_set_occurrences_add_occurrenceIDs_random():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceID='random')
    assert 'occurrenceID' in new_df.columns

def test_set_occurrences_add_occurrenceIDs_sequential():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'decimalLatitude': [1.0,1.0],
                       'decimalLongitude': [1.0,1.0]})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceID='sequential')
    assert 'occurrenceID' in new_df.columns

def test_set_occurrences_add_occurrenceIDs_composite():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceID=['eventDate','catalogNumber'])
    assert 'occurrenceID' in new_df.columns

def test_set_occurrences_add_occurrenceIDs_composite_random():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceID=['random','eventDate','catalogNumber'])
    assert 'occurrenceID' in new_df.columns

def test_set_occurrences_add_occurrenceIDs_composite_random_last():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceID=['eventDate','catalogNumber','random'])
    assert 'occurrenceID' in new_df.columns

def test_set_occurrences_add_occurrenceIDs_composite_sequential():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceID=['sequential','eventDate','catalogNumber'])
    assert 'occurrenceID' in new_df.columns

def test_set_occurrences_add_occurrenceIDs_composite_sequential_last():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'eventDate': ['2024-10-10','2024-10-10'],
                       'catalogNumber': ['1','2']})
    new_df = galaxias.set_occurrences(occurrences=df,occurrenceID=['eventDate','catalogNumber','sequential'])
    assert 'occurrenceID' in new_df.columns