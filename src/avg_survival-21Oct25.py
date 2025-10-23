import sys
import pandas as pd

df = load_csv(pd.read_csv('data/'))
print(df.head())
print(df.groupby('class').agg('mean', numeric))
