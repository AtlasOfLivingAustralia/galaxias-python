import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_scientific_name()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_scientific_name_no_arguments():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_scientific_name()
    assert "No Darwin Core" in str(e_info.value)

def test_set_scientific_name_rename():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_scientific_name(scientificName='species')
    assert 'scientificName' in occ_dwca.occurrences.columns

def test_set_scientific_name_incorrect_type():
    df = pd.DataFrame({'scientificName': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_scientific_name()
    assert "There are some errors" in str(e_info.value)

def test_set_scientific_name_incorrect_type_rename():
    df = pd.DataFrame({'species': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_scientific_name(scientificName='species')
    assert "There are some errors" in str(e_info.value)
