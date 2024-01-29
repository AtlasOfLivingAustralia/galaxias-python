# read version from installed package
from importlib.metadata import version
__version__ = version("galaxias")

# functions in package
from .dwca_build import dwca
#from .galaxias_config import galaxias_config

# get all functions to display
__all__=["dwca"]