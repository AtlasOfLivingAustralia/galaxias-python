# read version from installed package
from importlib.metadata import version
__version__ = version("galaxias")

# functions in package
#from .dwca import *
#from .galaxias import *
from .metadata import read_dwc_terms 
from .dwc_data import check_dwca_column_names,rename_dwc_columns,check_for_duplicates,check_dwca_column_formatting

# get all functions to display
__all__=["read_dwc_terms","check_dwca_column_names","rename_dwc_columns","check_for_duplicates",
         "check_dwca_column_formatting"]