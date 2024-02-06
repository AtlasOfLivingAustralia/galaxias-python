import galaxias
import pandas as pd
import sys

# get option
stopping_point = sys.argv[1]

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

data = pd.read_csv("galaxias_user_guide/data_clean.csv")
my_dwca = galaxias.dwca(occurrences=data)

# EML point
my_dwca.make_eml_xml()
if stopping_point == "eml":
    sys.exit()

my_dwca.make_meta_xml()