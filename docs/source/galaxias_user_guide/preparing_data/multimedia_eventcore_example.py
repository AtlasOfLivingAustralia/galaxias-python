import pandas as pd

# potentially take this out
import warnings
warnings.filterwarnings("ignore")

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

df = pd.DataFrame({'eventID': ['3','3','3','3','3','3'],
                   'occurrenceID': ['337FB2A8-1B76-4E58-9FC3-9E4EA952CA3B',
                                    'A5B778D4-D127-4B6F-8C72-21CE4DCDD2D7',
                                    'BD589526-86C0-4341-8F2C-821EB9AF989E',
                                    'C1E35DBF-5DE1-422A-B481-E57A413E5739',
                                    'FABBBB25-0073-45CC-8B4A-E24BFA76A30F',
                                    'FABBBB25-0073-45CC-8B4A-E24BFA76A30F'],
                   'identifier': ['https://link.to.photo/photo1.jpg',
                                  'https://link.to.photo/photo2.jpg',
                                  'https://link.to.photo/photo3.jpg',
                                  'https://link.to.photo/photo4.jpg',
                                  'https://link.to.photo/photo5.jpg',
                                  'https://link.to.photo/photo6.jpg',]})

print(df)