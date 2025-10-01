import galaxias
import pandas as pd

# set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

galaxias.use_metadata_template()
print(galaxias.display_metadata_as_dataframe())