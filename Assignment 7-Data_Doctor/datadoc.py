import pandas as pd

df = pd.read_csv("data.csv")

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize text
for col in df.select_dtypes(include='object'):
    df[col] = df[col].str.lower().str.strip()

print(df.head())