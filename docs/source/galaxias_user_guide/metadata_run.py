import galaxias
import pandas as pd

# set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

import os
my_dwca = galaxias.dwca(metadata_md='metadata.md',working_dir='./galaxias_user_guide/',print_notices=False)
print(my_dwca.display_metadata_as_dataframe())