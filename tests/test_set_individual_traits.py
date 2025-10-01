import pytest
import galaxias
import pandas as pd
import uuid

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        df = galaxias.set_individual_traits()
    assert "Please provide a dataframe" in str(e_info.value)

def test_individualID_not_string_UUID():
    df = pd.DataFrame({'individualID': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_individual_traits(dataframe=df)
    assert "individualID" in str(e_info.value)

def test_lifeStage_not_string():
    df = pd.DataFrame({'lifeStage': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_individual_traits(dataframe=df)
    assert "lifeStage" in str(e_info.value)

def test_sex_not_string():
    df = pd.DataFrame({'sex': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_individual_traits(dataframe=df)
    assert "sex" in str(e_info.value)

def test_vitality_not_string():
    df = pd.DataFrame({'vitality': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_individual_traits(dataframe=df)
    assert "vitality" in str(e_info.value)

def test_reproductiveCondition_not_string():
    df = pd.DataFrame({'reproductiveCondition': [1,1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_individual_traits(dataframe=df)
    assert "reproductiveCondition" in str(e_info.value)

def test_individualID_uuid():
    df = pd.DataFrame({'individualID': [uuid.uuid4(),uuid.uuid4()]})
    new_df = galaxias.set_individual_traits(dataframe=df)
    assert "individualID" in new_df.columns

def test_individualID_uuid_rename():
    df = pd.DataFrame({'id': [uuid.uuid4(),uuid.uuid4()]})
    new_df = galaxias.set_individual_traits(dataframe=df,individualID='id')
    assert "individualID" in new_df.columns

def test_individualID_list():
    df = pd.DataFrame({'individualID': ['1','1']})
    new_df = galaxias.set_individual_traits(dataframe=df)
    assert "individualID" in new_df.columns

def test_individualID_list_rename():
    df = pd.DataFrame({'id': ['1','1']})
    new_df = galaxias.set_individual_traits(dataframe=df,individualID='id')
    assert "individualID" in new_df.columns

def test_lifestage_sex_vitality_reprod_rename():
    df = pd.DataFrame({'individualID': ['1','1'], 'stage': ['baby','baby'], 'mf': ['male','female'], 'status': ['alive','alive'], 
                       'fertility': ['fertile','fertile']})
    new_df = galaxias.set_individual_traits(dataframe=df,lifeStage='stage',sex='mf',vitality='status',reproductiveCondition='fertility')
    assert all(x in new_df.columns for x in ['individualID','lifeStage','sex','vitality','reproductiveCondition'])

def test_lifestage_sex_vitality_reprod_list():
    df = pd.DataFrame({'individualID': ['1','1']})
    new_df = galaxias.set_individual_traits(dataframe=df,lifeStage=['baby','baby'],sex=['male','female'],
                                            vitality=['alive','alive'],reproductiveCondition=['fertile','fertile'])
    assert all(x in new_df.columns for x in ['individualID','lifeStage','sex','vitality','reproductiveCondition'])

def test_lifestage_sex_vitality_reprod_string():
    df = pd.DataFrame({'individualID': ['1','1']})
    new_df = galaxias.set_individual_traits(dataframe=df,lifeStage='baby',sex='female',vitality='alive',reproductiveCondition='fertile')
    assert all(x in new_df.columns for x in ['individualID','lifeStage','sex','vitality','reproductiveCondition'])