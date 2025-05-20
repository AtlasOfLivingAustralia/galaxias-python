import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_abundance()
    assert "Please provide a dataframe" in str(e_info.value)

def test_individualCount_not_numeric():
    df = pd.DataFrame({'individualCount': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_abundance()
    assert "numeric" in str(e_info.value)

def test_organismQuantity_not_numeric():
    df = pd.DataFrame({'organismQuantity': ['one','one'], 'organismQuantityType': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_abundance()
    assert "numeric" in str(e_info.value)

def test_organismQuantityType_not_string():
    df = pd.DataFrame({'organismQuantity': [1,1], 'organismQuantityType': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_abundance()
    assert "string" in str(e_info.value)

def test_individualCount_renamed():
    df = pd.DataFrame({'individuals': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_abundance(individualCount='individuals')
    assert 'individualCount' in occ_dwca.occurrences.columns

def test_individualCount_data():
    df = pd.DataFrame({'individualCount': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_abundance()
    assert "There are some errors" in str(e_info.value)

def test_individualCount_data_works():
    df = pd.DataFrame({'individualCount': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_abundance()
    assert type(occ_dwca.occurrences) is pd.DataFrame

def test_organismQuanitityType_organismQuantity_renamed():
    df = pd.DataFrame({'individualCount': [1,1],
                       'number': [1,1], 
                       'description': ['individual adult','individual adult']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_abundance(organismQuantity='number',organismQuantityType='description')
    assert all(x in occ_dwca.occurrences.columns for x in ['organismQuantityType','organismQuantity'])

def test_individualCount_organismQuanitityType_organismQuantity_renamed():
    df = pd.DataFrame({'individuals': [1,1],
                       'number': [1,1], 
                       'description': ['individual adult','individual adult']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_abundance(individualCount='individuals',organismQuantity='number',organismQuantityType='description')
    assert all(x in occ_dwca.occurrences.columns for x in ['individualCount','organismQuantityType','organismQuantity'])

def test_set_abundance_works():
    df = pd.DataFrame({'individualCount': [1,1], 
                       'organismQuantity': [1,1], 
                       'organismQuantityType': ['individual adult','individual adult']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_abundance()
    assert type(occ_dwca.occurrences) is pd.DataFrame