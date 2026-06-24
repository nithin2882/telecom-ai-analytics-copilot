import pandas as pd

df = pd.read_csv(
    "data/cleaned/telecom_clean.csv"
)

print("Rows:", len(df))

print(
    "Duplicates:",
    df.duplicated().sum()
)

print(
    "Negative Usage:",
    (df["data_used"] < 0).sum()
)