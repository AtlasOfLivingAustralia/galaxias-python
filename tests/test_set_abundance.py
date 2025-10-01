import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        df = galaxias.set_abundance()
    assert "Please provide a dataframe" in str(e_info.value)
    
def test_individualCount_not_numeric():
    df = pd.DataFrame({'individualCount': ['1','1']}) 
    with pytest.raises(Exception) as e_info:
        temp = galaxias.set_abundance(dataframe=df)
    assert "numeric" in str(e_info.value)

def test_organismQuantity_not_numeric():
    df = pd.DataFrame({'organismQuantity': ['one','one'], 'organismQuantityType': ['1','1']})
    with pytest.raises(Exception) as e_info:
        temp = galaxias.set_abundance(dataframe=df)
    assert "numeric" in str(e_info.value)

def test_organismQuantityType_not_string():
    df = pd.DataFrame({'organismQuantity': [1,1], 'organismQuantityType': [1,1]})
    with pytest.raises(Exception) as e_info:
        temp = galaxias.set_abundance(dataframe=df)
    assert "string" in str(e_info.value)

def test_individualCount_renamed():
    df = pd.DataFrame({'individuals': [1.0,1.0]})
    new_df = galaxias.set_abundance(dataframe=df,individualCount='individuals')
    assert 'individualCount' in new_df.columns

def test_individualCount_data():
    df = pd.DataFrame({'individualCount': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_abundance(dataframe=df)
    assert "There are some errors" in str(e_info.value)

def test_individualCount_data_works():
    df = pd.DataFrame({'individualCount': [1,1]})
    new_df = galaxias.set_abundance(dataframe=df)
    assert type(new_df) is pd.DataFrame

def test_organismQuanitityType_organismQuantity_renamed():
    df = pd.DataFrame({'individualCount': [1,1],
                       'number': [1,1], 
                       'description': ['individual adult','individual adult']})
    new_df = galaxias.set_abundance(dataframe=df,organismQuantity='number',organismQuantityType='description')
    assert all(x in new_df.columns for x in ['organismQuantityType','organismQuantity'])

def test_individualCount_organismQuanitityType_organismQuantity_renamed():
    df = pd.DataFrame({'individuals': [1,1],
                       'number': [1,1], 
                       'description': ['individual adult','individual adult']})
    new_df = galaxias.set_abundance(dataframe=df,individualCount='individuals',organismQuantity='number',organismQuantityType='description')
    assert all(x in new_df.columns for x in ['individualCount','organismQuantityType','organismQuantity'])

def test_set_abundance_works():
    df = pd.DataFrame({'individualCount': [1,1], 
                       'organismQuantity': [1,1], 
                       'organismQuantityType': ['individual adult','individual adult']})
    new_df = galaxias.set_abundance(dataframe=df)
    assert type(new_df) is pd.DataFrame