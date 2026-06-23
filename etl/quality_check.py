import pandas as pd


df = pd.read_csv(
    "data/raw/telecom_churn.csv"
)

print("\n========== DATA QUALITY REPORT ==========\n")

# Total records
print(f"Total Records: {len(df)}")

# Total columns
print(f"Total Columns: {len(df.columns)}")

# Missing values
print("\nMissing Values:")

missing = df.isnull().sum()

print(
    missing[missing > 0]
)

# Duplicate records
duplicates = df.duplicated().sum()

print(
    f"\nDuplicate Records: {duplicates}"
)

# Negative data usage
negative_usage = (
    df["data_used"] < 0
).sum()

print(
    f"\nNegative Data Usage Records: {negative_usage}"
)

# Invalid age
invalid_age = (
    (df["age"] < 18)
    |
    (df["age"] > 100)
).sum()

print(
    f"Invalid Age Records: {invalid_age}"
)

# Invalid churn values
invalid_churn = (
    ~df["churn"].isin([0, 1])
).sum()

print(
    f"Invalid Churn Values: {invalid_churn}"
)

print(
    "\n========== END OF REPORT ==========\n"
)