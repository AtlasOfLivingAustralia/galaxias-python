import galaxias
import pytest
import pandas as pd
import datetime

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        df = galaxias.set_datetime()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_datetime_no_arguments():
    df = pd.DataFrame({'latitude': [1.0,1.0],'decimalLongitude': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df)
    assert "No Darwin Core" in str(e_info.value)

def test_eventDate_renamed():
    df = pd.DataFrame({'date': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)]})
    new_df = galaxias.set_datetime(dataframe=df,eventDate='date')
    assert 'eventDate' in new_df.columns

def test_year_renamed():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'y': [2024,2024]})
    new_df = galaxias.set_datetime(dataframe=df,year='y')
    assert 'year' in new_df.columns

def test_month_renamed():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'm': [10,10]})
    new_df = galaxias.set_datetime(dataframe=df,month='m')
    assert 'month' in new_df.columns

def test_day_renamed():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'd': [10,10]})
    new_df = galaxias.set_datetime(dataframe=df,day='d')
    assert 'day' in new_df.columns

def test_eventTime_renamed():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'time': [datetime.time(10,10,10),datetime.time(10,10,10)]})
    new_df = galaxias.set_datetime(dataframe=df,eventTime='time')
    assert 'eventTime' in new_df.columns

def test_eventDate_invalid_datetime():
    df = pd.DataFrame({'eventDate': ['2024-10-10','2024-10-10']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df)
    assert "datetime" in str(e_info.value)

def test_eventDate_invalid_datetime_rename():
    df = pd.DataFrame({'date': ['2024-10-10','2024-10-10']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df,eventDate='date')
    assert "datetime" in str(e_info.value)

def test_year_invalid_format():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'year': ['2024','2024']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df)
    assert "year" in str(e_info.value)

def test__invalid_format_rename():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'y': ['2024','2024']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df,year='y')
    assert "year" in str(e_info.value)

def test_month_invalid_format():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'month': ['10','10']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df)
    assert "month" in str(e_info.value)

def test_month_invalid_format_rename():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'm': ['10','10']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df,month='m')
    assert "month" in str(e_info.value)

def test_day_invalid_format():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'day': ['10','10']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df)
    assert "day" in str(e_info.value)

def test_day_invalid_format_rename():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'd': ['10','10']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df,day='d')
    assert "day" in str(e_info.value)

def test_eventTime_invalid_datetime():
    df = pd.DataFrame({'eventDate': ['2024-10-10','2024-10-10'],
                       'eventTime': ['10:10:10','10:10:10']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df)
    assert "datetime" in str(e_info.value)

def test_eventTime_invalid_datetime_rename():
    df = pd.DataFrame({'eventDate': ['2024-10-10','2024-10-10'],
                       'time': ['10:10:10','10:10:10']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_datetime(dataframe=df,eventDate='time')
    assert "datetime" in str(e_info.value)

def test_eventDate_string_to_datetime():
    df = pd.DataFrame({'eventDate': ['2024-10-10','2024-10-10']})
    new_df = galaxias.set_datetime(dataframe=df,string_to_datetime=True,yearfirst=True)
    assert type(new_df) is pd.DataFrame

def test_eventTime_string_to_datetime():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'eventTime': ['10:10:10','10:10:10']})
    new_df = galaxias.set_datetime(dataframe=df,string_to_datetime=True,yearfirst=True)
    assert type(new_df) is pd.DataFrame