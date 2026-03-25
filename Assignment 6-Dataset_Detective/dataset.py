import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

print("Highest Avg Column:")
print(df.mean(numeric_only=True).idxmax())

print("Missing Values:")
print(df.isnull().sum())