# read version from installed package
from importlib.metadata import version
__version__ = version("galaxias")

# functions in package
from .galaxias import create_dwca,validate_dwca_ala,post_dwca_ala
from .metadata import read_dwc_terms,update_dwc_terms,update_eml_xml,create_metadata_file,write_eml_xml,write_meta_xml
from .dwc_data import check_spatial_validity,check_dwca_column_formatting,check_for_duplicates,check_dwca_column_names,check_species_names,rename_dwc_columns,add_column,add_taxonomic_information,change_species_names
from .galaxias_config import galaxias_config