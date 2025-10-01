import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_scientific_name()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_scientific_name_no_arguments():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_scientific_name(dataframe=df)
    assert "No Darwin Core" in str(e_info.value)

def test_set_scientific_name_rename():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    new_df = galaxias.set_scientific_name(dataframe=df,scientificName='species')
    assert 'scientificName' in new_df.columns

def test_set_scientific_name_incorrect_type():
    df = pd.DataFrame({'scientificName': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_scientific_name(dataframe=df)
    assert "There are some errors" in str(e_info.value)

def test_set_scientific_name_incorrect_type_rename():
    df = pd.DataFrame({'species': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_scientific_name(dataframe=df,scientificName='species')
    assert "There are some errors" in str(e_info.value)