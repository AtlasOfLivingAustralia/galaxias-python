import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        galaxias.set_locality()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_locality_no_arguments():
    df = pd.DataFrame({'latitude': [1.0,1.0],'decimalLongitude': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "No Darwin Core" in str(e_info.value)

def test_continent_renamed():
    df = pd.DataFrame({'cont': ['Oceania','Oceania']})
    new_df = galaxias.set_locality(dataframe=df,continent='cont')
    assert 'continent' in new_df.columns

def test_country_renamed():
    df = pd.DataFrame({'Country': ['Australia','Australia']})
    new_df = galaxias.set_locality(dataframe=df,country='Country')
    assert 'country' in new_df.columns

def test_countryCodes_renamed():
    df = pd.DataFrame({'codes': ['AU','AU']})
    new_df = galaxias.set_locality(dataframe=df,countryCode='codes')
    assert 'countryCode' in new_df.columns

def test_stateProvince_renamed():
    df = pd.DataFrame({'sp': ['ACT','ACT']})
    new_df = galaxias.set_locality(dataframe=df,stateProvince='sp')
    assert 'stateProvince' in new_df.columns

def test_locality_renamed():
    df = pd.DataFrame({'local': ['Canberra','Canberra']})
    new_df = galaxias.set_locality(dataframe=df,locality='locality')
    assert 'locality' in new_df.columns

def test_empty_dataframe_add_value():
    df = pd.DataFrame()
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df,continent='Oceania')
    assert "empty dataframe" in str(e_info.value)

def test_continent_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    new_df = galaxias.set_locality(dataframe=df,continent='Oceania')
    assert all(new_df['continent'] == 'Oceania')

def test_country_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    new_df = galaxias.set_locality(dataframe=df,country='Australia')
    assert all(new_df['country'] == 'Australia')

def test_countryCodes_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    new_df = galaxias.set_locality(dataframe=df,countryCode='AU')
    assert all(new_df['countryCode'] == 'AU')

def test_stateProvince_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    new_df = galaxias.set_locality(dataframe=df,stateProvince='ACT')
    assert all(new_df['stateProvince'] == 'ACT')

def test_locality_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    new_df = galaxias.set_locality(dataframe=df,locality='Canberra')
    assert all(new_df['locality'] == 'Canberra')

def test_continent_wrong_type():
    df = pd.DataFrame({'continent': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "continent" in str(e_info.value)

def test_country_wrong_type():
    df = pd.DataFrame({'country': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "country" in str(e_info.value)

def test_countryCodes_wrong_type():
    df = pd.DataFrame({'countryCode': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "countryCode" in str(e_info.value)

def test_stateProvince_wrong_type():
    df = pd.DataFrame({'stateProvince': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "stateProvince" in str(e_info.value)

def test_locality_wrong_type():
    df = pd.DataFrame({'locality': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "locality" in str(e_info.value)

def test_continent_wrong_value():
    df = pd.DataFrame({'continent': ['Australia','Australia']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "continent" in str(e_info.value)

def test_country_wrong_value():
    df = pd.DataFrame({'country': ['Austr','Austr']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "country" in str(e_info.value)

def test_countryCodes_wrong_value():
    df = pd.DataFrame({'countryCode': ['AB','AB']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_locality(dataframe=df)
    assert "countryCode" in str(e_info.value)