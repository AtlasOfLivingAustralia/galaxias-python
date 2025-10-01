import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_license()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_license_no_arguments():
    df = pd.DataFrame({'lic.': ['CC-BY 4.0','CC-BY 4.0']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_license(dataframe=df)
    assert "No Darwin Core" in str(e_info.value)

def test_set_license_rename():
    df = pd.DataFrame({'lic.': ['CC-BY 4.0','CC-BY 4.0']})
    new_df = galaxias.set_license(dataframe=df,license='lic.')
    assert 'license' in new_df.columns

def test_set_license_incorrect_type():
    df = pd.DataFrame({'license': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_license(dataframe=df)
    assert "There are some errors" in str(e_info.value)

def test_set_license_incorrect_type_rename():
    df = pd.DataFrame({'lic.': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_license(dataframe=df,license='lic.')
    assert "There are some errors" in str(e_info.value)