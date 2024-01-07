import galaxias
import pandas as pd

def test_config():
   default_config = galaxias.galaxias_config()
   assert default_config is not None

def test_config_set_value():
   galaxias.galaxias_config(atlas="GBIF")
   GBIF_config = galaxias.galaxias_config()
   value = GBIF_config[GBIF_config["Configuration"] == "atlas"]["Value"][0]
   assert value == "GBIF"

def test_check_dwca_column_names_false():
   galaxias.galaxias_config(atlas="Australia")
   data = pd.read_csv("data_wrong_names.csv")
   column_names_check = galaxias.check_dwca_column_names(dataframe=data)
   assert not column_names_check

def test_check_dwca_column_names_false():
   galaxias.galaxias_config(atlas="Australia")
   data = pd.read_csv("data_correct_names.csv")
   column_names_check = galaxias.check_dwca_column_names(dataframe=data)
   assert column_names_check