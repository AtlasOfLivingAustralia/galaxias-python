import galaxias

def test_config():
   default_config = galaxias.galaxias_config()
   assert default_config is not None

def test_config_set_value():
    galaxias.galaxias_config(atlas="GBIF")
    GBIF_config = galaxias.galaxias_config()
    value = GBIF_config[GBIF_config["Configuration"] == "atlas"]["Value"][0]
    assert value == "GBIF"