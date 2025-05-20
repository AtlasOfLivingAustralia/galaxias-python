import galaxias
import pandas as pd

# read in data
data = pd.read_csv("tests/example/occurrence_data_USE.csv")

# check for duplicate DwCA terms
galaxias.check_for_duplicates(dataframe=data)

# check columns for DwCA compliance
galaxias.check_dwca_column_names(dataframe=data)

# rename data columns
new_data = galaxias.rename_dwc_columns(dataframe=data,names={"Species": "scientificName","Site": "locationID","Latitude": "decimalLatitude","Longitude": "decimalLongitude","Reference(s)": "references","Collection_date": "eventDate"})
galaxias.check_dwca_column_names(dataframe=new_data)

# add required columns that are missing
new_data_bor = galaxias.add_column(dataframe=new_data,column_name="basisOfRecord",value="HUMAN_OBSERVATION")
new_data_bor_oid = galaxias.add_column(dataframe=new_data_bor,column_name="occurrenceID")
new_data_bor_oid_geo = galaxias.add_column(dataframe=new_data_bor_oid,column_name="geodeticDatum",value="WGS84")
new_data_bor_oid_geo_coord_uncertainty = galaxias.add_column(dataframe=new_data_bor_oid_geo,column_name="coordinateUncertaintyInMeters",value="100")

# check species names
galaxias.check_species_names(dataframe=new_data,replace_old_names = True)
new_data_species_rename = galaxias.change_species_names(dataframe=new_data,species_changes={"Thysanotus sp": "Thysanotus sp. Yellowdine (A.S.George 6040)","Scaevola": "Scaevola hookeri", "Stylidium sp": "Stylidium sp. Banovich Road (F. & J.Hort 1884)"})
new_data_species_rename_taxonomy = galaxias.add_taxonomic_information(dataframe=new_data_species_rename)

# check spatial validity
galaxias.check_spatial_validity(dataframe=new_data_species_rename_taxonomy)

# check column formatting
galaxias.check_dwca_column_formatting(dataframe = new_data_species_rename_taxonomy)