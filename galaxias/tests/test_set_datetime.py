import galaxias
import pytest
import pandas as pd
import datetime

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_datetime_no_arguments():
    df = pd.DataFrame({'latitude': [1.0,1.0],'decimalLongitude': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime()
    assert "No Darwin Core" in str(e_info.value)

def test_eventDate_renamed():
    df = pd.DataFrame({'date': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_datetime(eventDate='date')
    assert 'eventDate' in occ_dwca.occurrences.columns

def test_year_renamed():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'y': [2024,2024]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_datetime(year='y')
    assert 'year' in occ_dwca.occurrences.columns

def test_month_renamed():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'm': [10,10]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_datetime(month='m')
    assert 'month' in occ_dwca.occurrences.columns

def test_day_renamed():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'd': [10,10]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_datetime(day='d')
    assert 'day' in occ_dwca.occurrences.columns

def test_eventTime_renamed():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'time': [datetime.time(10,10,10),datetime.time(10,10,10)]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_datetime(eventTime='time')
    assert 'eventTime' in occ_dwca.occurrences.columns

def test_eventDate_invalid_datetime():
    df = pd.DataFrame({'eventDate': ['2024-10-10','2024-10-10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime()
    assert "datetime" in str(e_info.value)

def test_eventDate_invalid_datetime_rename():
    df = pd.DataFrame({'date': ['2024-10-10','2024-10-10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime(eventDate='date')
    assert "datetime" in str(e_info.value)

def test_year_invalid_format():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'year': ['2024','2024']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime()
    assert "year" in str(e_info.value)

def test__invalid_format_rename():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'y': ['2024','2024']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime(year='y')
    assert "year" in str(e_info.value)

def test_month_invalid_format():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'month': ['10','10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime()
    assert "month" in str(e_info.value)

def test_month_invalid_format_rename():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'm': ['10','10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime(month='m')
    assert "month" in str(e_info.value)

def test_day_invalid_format():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'day': ['10','10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime()
    assert "day" in str(e_info.value)

def test_day_invalid_format_rename():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'd': ['10','10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime(day='d')
    assert "day" in str(e_info.value)

def test_eventTime_invalid_datetime():
    df = pd.DataFrame({'eventDate': ['2024-10-10','2024-10-10'],
                       'eventTime': ['10:10:10','10:10:10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime()
    assert "datetime" in str(e_info.value)

def test_eventTime_invalid_datetime_rename():
    df = pd.DataFrame({'eventDate': ['2024-10-10','2024-10-10'],
                       'time': ['10:10:10','10:10:10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_datetime(eventDate='time')
    assert "datetime" in str(e_info.value)

def test_eventDate_string_to_datetime():
    df = pd.DataFrame({'eventDate': ['2024-10-10','2024-10-10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_datetime(string_to_datetime=True,yearfirst=True)
    assert type(occ_dwca.occurrences) is pd.DataFrame

def test_eventTime_string_to_datetime():
    df = pd.DataFrame({'eventDate': [datetime.datetime(2024,10,10),datetime.datetime(2024,10,10)],
                       'eventTime': ['10:10:10','10:10:10']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_datetime(string_to_datetime=True,yearfirst=True)
    assert type(occ_dwca.occurrences) is pd.DataFrame