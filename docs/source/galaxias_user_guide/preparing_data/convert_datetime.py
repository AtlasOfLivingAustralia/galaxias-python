# DD-MM-YYYY
import pandas as pd
dates =  pd.DataFrame(
    {
        "eventDate": ["05-01-2005","22-02-2022","5-5-2005","21-9-2021"]
    }
)
for i,row in dates.iterrows():
    split_date = row["eventDate"].split("-")
    dates.at[i,"eventDate"] = "-".join(list(reversed(split_date)))
print(dates)