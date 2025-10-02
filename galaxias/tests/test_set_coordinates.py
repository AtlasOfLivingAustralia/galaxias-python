import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    with pytest.raises(Exception) as e_info:
        df = galaxias.set_coordinates()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_coordinates_no_arguments():
    df = pd.DataFrame({'latitude': [1.0,1.0],'longitude': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        temp = galaxias.set_datetime(dataframe=df)
    assert "No Darwin Core" in str(e_info.value)

def test_not_both_decimalLatitude_decimalLongitude():
    df = pd.DataFrame({'latitude': [1.0,1.0],'decimalLongitude': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        temp = galaxias.set_coordinates(dataframe=df)
    assert "You need to provide both" in str(e_info.value)

def test_decimalLatitude_renamed():
    df = pd.DataFrame({'latitude': [1.0,1.0],'decimalLongitude': [1.0,1.0]})
    new_df = galaxias.set_coordinates(dataframe=df,decimalLatitude='latitude')
    assert 'decimalLatitude' in new_df.columns

def test_decimalLongitude_renamed():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'longitude': [1.0,1.0]})
    new_df = galaxias.set_coordinates(dataframe=df,decimalLongitude='longitude')
    assert 'decimalLongitude' in new_df.columns

def test_geodeticDatum_renamed():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'crs': ['WGS84','WGS84']})
    new_df = galaxias.set_coordinates(dataframe=df,geodeticDatum='crs')
    assert 'geodeticDatum' in new_df.columns

def test_coordinateUncertaintyInMeters_renamed():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'uncertainty': [1.0,1.0]})
    new_df = galaxias.set_coordinates(dataframe=df,coordinateUncertaintyInMeters='uncertainty')
    assert 'coordinateUncertaintyInMeters' in new_df.columns

def test_coordinatePrecision_renamed():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'uncertainty': [1.0,1.0]})
    new_df = galaxias.set_coordinates(dataframe=df,coordinatePrecision='uncertainty')
    assert 'coordinatePrecision' in new_df.columns

def test_decimalLatitude_decimalLongitude_renamed():
    df = pd.DataFrame({'latitude': [1.0,1.0],
                       'longitude': [1.0,1.0]})
    new_df = galaxias.set_coordinates(dataframe=df,decimalLatitude='latitude',decimalLongitude='longitude')
    assert all(x in new_df.columns for x in ['decimalLatitude','decimalLongitude'])

def test_decimalLatitude_decimalLongitude_geodeticDatum_renamed():
    df = pd.DataFrame({'latitude': [1.0,1.0],
                       'longitude': [1.0,1.0],
                       'crs': ['WGS84','WGS84']})
    new_df = galaxias.set_coordinates(dataframe=df,decimalLatitude='latitude',decimalLongitude='longitude',geodeticDatum='crs')
    assert all(x in new_df.columns for x in ['decimalLatitude','decimalLongitude','geodeticDatum'])

def test_decimalLatitude_decimalLongitude_geodeticDatum_coordinateUncertaintyInMeters_renamed():
    df = pd.DataFrame({'latitude': [1.0,1.0],
                       'longitude': [1.0,1.0],
                       'crs': ['WGS84','WGS84'],
                       'uncertainty': [1.0,1.0]})
    new_df = galaxias.set_coordinates(dataframe=df,decimalLatitude='latitude',decimalLongitude='longitude',
                                      geodeticDatum='crs',coordinateUncertaintyInMeters='uncertainty')
    assert all(x in new_df.columns for x in ['decimalLatitude','decimalLongitude','geodeticDatum','coordinateUncertaintyInMeters'])

def test_decimalLatitude_decimalLongitude_geodeticDatum_coordinateUncertaintyInMeters_coordinatePrecision_renamed():
    df = pd.DataFrame({'latitude': [1.0,1.0],
                       'longitude': [1.0,1.0],
                       'crs': ['WGS84','WGS84'],
                       'uncertainty': [1.0,1.0],
                       'uncertainty_deg': [1.0,1.0]})
    new_df = galaxias.set_coordinates(dataframe=df,decimalLatitude='latitude',decimalLongitude='longitude',
                                      geodeticDatum='crs',coordinateUncertaintyInMeters='uncertainty',
                                      coordinatePrecision='uncertainty_deg')
    assert all(x in new_df.columns for x in ['decimalLatitude','decimalLongitude','geodeticDatum','coordinateUncertaintyInMeters','coordinatePrecision'])

def test_decimalLatitude_invalid_format():
    df = pd.DataFrame({'decimalLatitude': ['1.0','1.0'],'decimalLongitude': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        temp = galaxias.set_coordinates(dataframe=df)
    assert "numeric" in str(e_info.value)

def test_decimalLatitude_invalid_format_rename():
    df = pd.DataFrame({'latitude': ['1.0','1.0'],'decimalLongitude': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df,decimalLatitude='latitude')
    assert "numeric" in str(e_info.value)

def test_decimalLongitude_invalid_format():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': ['1.0','1.0']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df)
    assert "numeric" in str(e_info.value)

def test_decimalLongitude_invalid_format_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'longitude': ['1.0','1.0']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df,decimalLatitude='longitude')
    assert "numeric" in str(e_info.value)

def test_geodeticDatum_invalid_format():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': ['1.0','1.0'],'geodeticDatum': [4326,4326]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df)
    assert "numeric" in str(e_info.value)

def test_geodeticDatum_invalid_format_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'crs': [4326,4326]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df,geodeticDatum='crs')
    assert "string" in str(e_info.value)

def test_coordinateUncertaintyInMeters_invalid_format():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'coordinateUncertaintyInMeters': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df)
    assert "numeric" in str(e_info.value)

def test_coordinateUncertaintyInMeters_invalid_format_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'uncertainty': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df,coordinateUncertaintyInMeters='uncertainty')
    assert "numeric" in str(e_info.value)

def test_coordinatePrecision_invalid_format():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'coordinatePrecision': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df)
    assert "numeric" in str(e_info.value)

def test_coordinatePrecision_invalid_format_rename():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'uncertainty': ['1','1']})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df,coordinatePrecision='uncertainty')
    assert "numeric" in str(e_info.value)

def test_decimalLatitude_out_of_range():
    df = pd.DataFrame({'decimalLatitude': [91.0,91.0],'decimalLongitude': [1.0,1.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df)
    assert "There are some invalid" in str(e_info.value)

def test_decimalLongitude_out_of_range():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [181.0,181.0]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df)
    assert "There are some invalid" in str(e_info.value)

def test_coordinateUncertaintyInMeters_out_of_range():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'coordinateUncertaintyInMeters': [-1,-1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df)
    assert "There are some invalid" in str(e_info.value)

def test_coordinatePrecision_out_of_range():
    df = pd.DataFrame({'decimalLatitude': [1.0,1.0],'decimalLongitude': [1.0,1.0],'coordinatePrecision': [-1,-1]})
    with pytest.raises(Exception) as e_info:
        new_df = galaxias.set_coordinates(dataframe=df)
    assert "There are some invalid" in str(e_info.value)