import galaxias
import pytest
import pandas as pd
import uuid

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        df = galaxias.set_collection()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_collection_no_arguments():
    df = pd.DataFrame({'id': [uuid.uuid4(),uuid.uuid4()]})
    with pytest.raises(Exception) as e_info:
        temp = galaxias.set_collection(dataframe=df)
    assert "No Darwin Core" in str(e_info.value)

def test_set_collection_rename_datasetID():
    df = pd.DataFrame({'id': [uuid.uuid4(),uuid.uuid4()]})
    new_df = galaxias.set_collection(dataframe=df,datasetID='id')
    assert 'datasetID' in new_df.columns

def test_set_collection_column_string():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    new_df = galaxias.set_collection(dataframe=df,datasetID=uuid.uuid4())
    assert 'datasetID' in new_df.columns

def test_set_collection_column_list():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    new_df = galaxias.set_collection(dataframe=df,datasetID=[uuid.uuid4(),uuid.uuid4()])
    assert 'datasetID' in new_df.columns

def test_set_collection_incorrect_type_rename():
    df = pd.DataFrame({'id': [1,1]})
    with pytest.raises(Exception) as e_info:
        temp = galaxias.set_collection(dataframe=df,datasetID='id')
    assert "There are some errors" in str(e_info.value)

def test_set_collection_string_and_lists():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    new_df = galaxias.set_collection(dataframe=df,datasetID=uuid.uuid4(),datasetName='Test',catalogNumber='Test Catalog Number')
    assert all(x in new_df.columns for x in ['datasetID','datasetName','catalogNumber'])

def test_set_collection_string_and_lists_2():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    new_df = galaxias.set_collection(dataframe=df,datasetID=[uuid.uuid4(),uuid.uuid4()],datasetName=['Test','Test'],
                                     catalogNumber=['Test Catalog Number','Test Catalog Number'])
    assert all(x in new_df.columns for x in ['datasetID','datasetName','catalogNumber'])
