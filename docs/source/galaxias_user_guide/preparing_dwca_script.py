import galaxias
import pandas as pd
import sys
import datetime

# get option
stopping_point = sys.argv[1]

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# --------------------------------------------------------
# Part 1
# --------------------------------------------------------

# read in data
my_dwca = galaxias.dwca(occurrences="galaxias_user_guide/occurrences_dwc_clean.csv")

# start with one test
my_dwca.check_data()

# my_dwca.create_dwca()