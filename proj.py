import pandas as pd

# Load the full dataset
df = pd.read_csv("IPL.csv")

# See what you're working with
print(df.shape)        # how many rows and columns
print(df.columns.tolist())   # column names
print(df.head())       # first 5 rows