import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        galaxias.set_observer()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_observer_no_arguments():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_observer(dataframe=df)
    assert "No Darwin Core" in str(e_info.value)

def test_set_observer_rename():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'observer': ['David Attenborough','David Attenborough']})
    new_df = galaxias.set_observer(dataframe=df,recordedBy='observer')
    assert 'recordedBy' in new_df.columns

def test_set_observer_incorrect_type():
    df = pd.DataFrame({'recordedBy': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_observer(dataframe=df)
    assert "There are some errors" in str(e_info.value)

def test_set_observer_incorrect_type_rename():
    df = pd.DataFrame({'observer': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_observer(dataframe=df,recordedBy='observer')
    assert "There are some errors" in str(e_info.value)