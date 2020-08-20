import pandas as pd 

data = pd.read_csv("data/data.csv")

print(data.head())

data.drop(["quote_id", "quote_num"], inplace=True, axis=1)

data.to_csv("data/data.csv")

print(data.head())