from lat_lon_parser import parse
import pandas as pd 

# set dataframe
df = pd.DataFrame(
    {
        'decimalLatitude': ["35\° 50' 11\"", "45\° 51' 13\"", "30\° 20' 10\""], 
        'decimalLongitude': ["138\° 01\' 26\"", "139\° 11\' 16\"", "128\° 05\' 29\""]
    }
)

for i, row in df.iterrows():
    df.at[i, 'decimalLatitude'] = round(parse(row['decimalLatitude']), 2)
    df.at[i, 'decimalLongitude'] = round(parse(row['decimalLongitude']), 2)
print(df)