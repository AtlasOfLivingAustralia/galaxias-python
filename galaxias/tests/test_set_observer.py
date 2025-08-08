import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_observer()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_observer_no_arguments():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_observer()
    assert "No Darwin Core" in str(e_info.value)

def test_set_observer_rename():
    df = pd.DataFrame({'species': ['Eolophus roseicapilla','Eolophus roseicapilla'],
                       'observer': ['David Attenborough','David Attenborough']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_observer(recordedBy='observer')
    assert 'recordedBy' in occ_dwca.occurrences.columns

def test_set_observer_incorrect_type():
    df = pd.DataFrame({'recordedBy': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_observer()
    assert "There are some errors" in str(e_info.value)

def test_set_observer_incorrect_type_rename():
    df = pd.DataFrame({'observer': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_observer(recordedBy='observer')
    assert "There are some errors" in str(e_info.value)
