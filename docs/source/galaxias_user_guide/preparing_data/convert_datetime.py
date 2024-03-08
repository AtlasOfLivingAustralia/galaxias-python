# DD-MM-YYYY
import pandas as pd
import galaxias
import datetime
import sys

stopping_point = sys.argv[1]

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

if stopping_point == "1":
    dates =  pd.DataFrame(
        {
            "eventDate": ["05-01-2005","22-02-2022","5-5-2005","21-9-2021"]
        }
    )
    for i,row in dates.iterrows():
        split_date = list(map(int, row["eventDate"].split("-")))
        dates.at[i,"eventDate"] = datetime.date(split_date[2],split_date[1],split_date[0])
    print(dates)

if stopping_point == "2":

    data = pd.read_csv("galaxias_user_guide/occurrences_dwc_rename.csv")
    my_dwca = galaxias.dwca(occurrences=data)
    for i,row in my_dwca.occurrences.iterrows():
        split_date = list(map(int, row["eventDate"].split("/")))
        my_dwca.occurrences.at[i,"eventDate"] = str(datetime.date(split_date[2],split_date[1],split_date[0]))
    print(my_dwca.occurrences.head())