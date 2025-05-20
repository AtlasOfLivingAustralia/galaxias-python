import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_license()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_license_no_arguments():
    df = pd.DataFrame({'lic.': ['CC-BY 4.0','CC-BY 4.0']})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_license()
    assert "No Darwin Core" in str(e_info.value)

def test_set_license_rename():
    df = pd.DataFrame({'lic.': ['CC-BY 4.0','CC-BY 4.0']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_license(license='lic.')
    assert 'license' in occ_dwca.occurrences.columns

def test_set_license_incorrect_type():
    df = pd.DataFrame({'license': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_license()
    assert "There are some errors" in str(e_info.value)

def test_set_license_incorrect_type_rename():
    df = pd.DataFrame({'lic.': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_license(license='lic.')
    assert "There are some errors" in str(e_info.value)