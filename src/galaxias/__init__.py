# read version from installed package
from importlib.metadata import version
__version__ = version("galaxias")

# functions in package
#from .dwca import *
#from .galaxias import *
from .metadata import read_dwc_terms #,update_dwc_terms
#from .dwc_data import *

# get all functions to display
__all__=["read_dwc_terms"]