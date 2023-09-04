# read version from installed package
from importlib.metadata import version
__version__ = version("galaxias")

# functions in package
from .galaxias import *
from .metadata import *
from .dwc_data import *