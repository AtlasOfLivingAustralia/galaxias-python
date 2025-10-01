import galaxias
import pandas as pd
import pytest

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        df = galaxias.set_events()
    assert "Please provide a dataframe" in str(e_info.value)

def test_eventID_rename():
    df = pd.DataFrame({'id': ['1','2']})
    new_df = galaxias.set_events(dataframe=df,eventID='id')
    assert 'eventID' in new_df.columns

def test_eventID_no_parentEventID():
    df = pd.DataFrame({'id': ['1','2']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_events(dataframe=df,parentEventID='id')
    assert "parentEventID" in str(e_info.value)

def test_eventID_parentEventID_rename():
    df = pd.DataFrame({'id': ['1','2'], 'id_2': ['1','1']})
    new_df = galaxias.set_events(dataframe=df,eventID='id',parentEventID='id_2')
    assert all(x in new_df.columns for x in ['eventID','parentEventID'])

def test_set_eventType():
    df = pd.DataFrame({'eventID': ['1','2']})
    new_df = galaxias.set_events(dataframe=df,eventType='Survey')
    assert 'eventType' in new_df.columns

def test_set_Event():
    df = pd.DataFrame({'eventID': ['1','2']})
    new_df = galaxias.set_events(dataframe=df,Event='Survey')
    assert 'Event' in new_df.columns

def test_set_SamplingProtocol():
    df = pd.DataFrame({'eventID': ['1','2']})
    new_df = galaxias.set_events(dataframe=df,samplingProtocol='Survey and Observation')
    assert 'samplingProtocol' in new_df.columns

def test_set_event_hierarchy():
    df = pd.DataFrame({'Event': ['Survey','Survey']})
    new_df = galaxias.set_events(dataframe=df,event_hierarchy={1: 'Site Visit', 2: 'Sample', 3: 'Observation'})