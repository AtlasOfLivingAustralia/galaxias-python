import pandas as pd

# potentially take this out
import warnings
warnings.filterwarnings("ignore")

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

df = pd.DataFrame({'eventID': ['3','3','3','3','3'],
                   'occurrenceID': ['337FB2A8-1B76-4E58-9FC3-9E4EA952CA3B',
                                    'A5B778D4-D127-4B6F-8C72-21CE4DCDD2D7',
                                    'BD589526-86C0-4341-8F2C-821EB9AF989E',
                                    'C1E35DBF-5DE1-422A-B481-E57A413E5739',
                                    'FABBBB25-0073-45CC-8B4A-E24BFA76A30F'],
                   'measurementID': ['101',
                                  '102',
                                  '103',
                                  '104',
                                  '105'],
                    'measurementType': ['wingspan',
                                  'wingspan',
                                  'wingspan',
                                  'wingspan',
                                  'wingspan'],
                    'measurementValue': ['10',
                                  '12',
                                  '11',
                                  '14',
                                  '11'],
                    'measurementUnit': ['cm',
                                  'cm',
                                  'cm',
                                  'cm',
                                  'cm'],
                    'measurementUnit': ['0.1',
                                  '0.1',
                                  '0.1',
                                  '0.1',
                                  '0.1']})

print(df)