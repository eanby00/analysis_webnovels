import pandas as pd

df = pd.read_csv("./data_sample/munpia_novel_list_1.csv")
print(df.head())

df["favorit_per_day"] = df["favorite"] / df["serial_time"]

print(df.head())