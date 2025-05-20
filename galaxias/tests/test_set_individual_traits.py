import pytest
import galaxias
import pandas as pd
import uuid

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_individual_traits()
    assert "Please provide a dataframe" in str(e_info.value)

def test_individualID_not_string_UUID():
    df = pd.DataFrame({'individualID': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_individual_traits()
    assert "individualID" in str(e_info.value)

def test_lifeStage_not_string():
    df = pd.DataFrame({'lifeStage': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_individual_traits()
    assert "lifeStage" in str(e_info.value)

def test_sex_not_string():
    df = pd.DataFrame({'sex': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_individual_traits()
    assert "sex" in str(e_info.value)

def test_vitality_not_string():
    df = pd.DataFrame({'vitality': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_individual_traits()
    assert "vitality" in str(e_info.value)

def test_reproductiveCondition_not_string():
    df = pd.DataFrame({'reproductiveCondition': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_individual_traits()
    assert "reproductiveCondition" in str(e_info.value)

def test_individualID_uuid():
    df = pd.DataFrame({'individualID': [uuid.uuid4(),uuid.uuid4()]})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_individual_traits()
    assert "individualID" in occ_dwca.occurrences.columns

def test_individualID_uuid_rename():
    df = pd.DataFrame({'id': [uuid.uuid4(),uuid.uuid4()]})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_individual_traits(individualID='id')
    assert "individualID" in occ_dwca.occurrences.columns

def test_individualID_list():
    df = pd.DataFrame({'individualID': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_individual_traits()
    assert "individualID" in occ_dwca.occurrences.columns

def test_individualID_list_rename():
    df = pd.DataFrame({'id': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_individual_traits(individualID='id')
    assert "individualID" in occ_dwca.occurrences.columns

def test_lifestage_sex_vitality_reprod_rename():
    df = pd.DataFrame({'individualID': ['1','1'], 'stage': ['baby','baby'], 'mf': ['male','female'], 'status': ['alive','alive'], 
                       'fertility': ['fertile','fertile']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_individual_traits(lifeStage='stage',sex='mf',vitality='status',reproductiveCondition='fertility')
    assert all(x in occ_dwca.occurrences.columns for x in ['individualID','lifeStage','sex','vitality','reproductiveCondition'])

def test_lifestage_sex_vitality_reprod_list():
    df = pd.DataFrame({'individualID': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_individual_traits(lifeStage=['baby','baby'],sex=['male','female'],
                                           vitality=['alive','alive'],reproductiveCondition=['fertile','fertile'])
    assert all(x in occ_dwca.occurrences.columns for x in ['individualID','lifeStage','sex','vitality','reproductiveCondition'])

def test_lifestage_sex_vitality_reprod_string():
    df = pd.DataFrame({'individualID': ['1','1']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_individual_traits(lifeStage='baby',sex='female',vitality='alive',reproductiveCondition='fertile')
    assert all(x in occ_dwca.occurrences.columns for x in ['individualID','lifeStage','sex','vitality','reproductiveCondition'])