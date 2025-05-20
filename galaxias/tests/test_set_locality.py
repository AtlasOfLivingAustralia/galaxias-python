import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_locality_no_arguments():
    df = pd.DataFrame({'latitude': [1.0,1.0],'decimalLongitude': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "No Darwin Core" in str(e_info.value)

def test_continent_renamed():
    df = pd.DataFrame({'cont': ['Oceania','Oceania']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(continent='cont')
    assert 'continent' in occ_dwca.occurrences.columns

def test_country_renamed():
    df = pd.DataFrame({'Country': ['Australia','Australia']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(country='Country')
    assert 'country' in occ_dwca.occurrences.columns

def test_countryCodes_renamed():
    df = pd.DataFrame({'codes': ['AU','AU']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(countryCode='codes')
    assert 'countryCode' in occ_dwca.occurrences.columns

def test_stateProvince_renamed():
    df = pd.DataFrame({'sp': ['ACT','ACT']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(stateProvince='sp')
    assert 'stateProvince' in occ_dwca.occurrences.columns

def test_locality_renamed():
    df = pd.DataFrame({'local': ['Canberra','Canberra']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(locality='locality')
    assert 'locality' in occ_dwca.occurrences.columns

def test_empty_dataframe_add_value():
    df = pd.DataFrame()
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality(continent='Oceania')
    assert "empty dataframe" in str(e_info.value)

def test_continent_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(continent='Oceania')
    assert all(occ_dwca.occurrences['continent'] == 'Oceania')

def test_country_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(country='Australia')
    assert all(occ_dwca.occurrences['country'] == 'Australia')

def test_countryCodes_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(countryCode='AU')
    assert all(occ_dwca.occurrences['countryCode'] == 'AU')

def test_stateProvince_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(stateProvince='ACT')
    assert all(occ_dwca.occurrences['stateProvince'] == 'ACT')

def test_locality_add():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0], 'decimalLongitude': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    occ_dwca.set_locality(locality='Canberra')
    assert all(occ_dwca.occurrences['locality'] == 'Canberra')

def test_continent_wrong_type():
    df = pd.DataFrame({'continent': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "continent" in str(e_info.value)

def test_country_wrong_type():
    df = pd.DataFrame({'country': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "country" in str(e_info.value)

def test_countryCodes_wrong_type():
    df = pd.DataFrame({'countryCode': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "countryCode" in str(e_info.value)

def test_stateProvince_wrong_type():
    df = pd.DataFrame({'stateProvince': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "stateProvince" in str(e_info.value)

def test_locality_wrong_type():
    df = pd.DataFrame({'locality': [1.0,1.0]})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "locality" in str(e_info.value)

def test_continent_wrong_value():
    df = pd.DataFrame({'continent': ['Australia','Australia']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "continent" in str(e_info.value)

def test_country_wrong_value():
    df = pd.DataFrame({'country': ['Austr','Austr']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "country" in str(e_info.value)

def test_countryCodes_wrong_value():
    df = pd.DataFrame({'countryCode': ['AB','AB']})
    occ_dwca = galaxias.dwca(occurrences=df,create_md=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_locality()
    assert "countryCode" in str(e_info.value)