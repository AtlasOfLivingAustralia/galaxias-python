import galaxias
import pytest
import pandas as pd
import uuid

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_collection()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_collection_no_arguments():
    df = pd.DataFrame({'id': [uuid.uuid4(),uuid.uuid4()]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_collection()
    assert "No Darwin Core" in str(e_info.value)

def test_set_collection_rename_datasetID():
    df = pd.DataFrame({'id': [uuid.uuid4(),uuid.uuid4()]})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_collection(datasetID='id')
    assert 'datasetID' in occ_dwca.occurrences.columns

def test_set_collection_column_string():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_collection(datasetID=uuid.uuid4())
    assert 'datasetID' in occ_dwca.occurrences.columns

def test_set_collection_column_list():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_collection(datasetID=[uuid.uuid4(),uuid.uuid4()])
    assert 'datasetID' in occ_dwca.occurrences.columns

def test_set_collection_incorrect_type_rename():
    df = pd.DataFrame({'id': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_collection(datasetID='id')
    assert "There are some errors" in str(e_info.value)

def test_set_collection_string_and_lists():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_collection(datasetID=uuid.uuid4(),datasetName='Test',catalogNumber='Test Catalog Number')
    assert all(x in occ_dwca.occurrences.columns for x in ['datasetID','datasetName','catalogNumber'])

def test_set_collection_string_and_lists():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_collection(datasetID=[uuid.uuid4(),uuid.uuid4()],datasetName=['Test','Test'],
                                    catalogNumber=['Test Catalog Number','Test Catalog Number'])
    assert all(x in occ_dwca.occurrences.columns for x in ['datasetID','datasetName','catalogNumber'])