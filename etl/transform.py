import pandas as pd

df = pd.read_csv(
    "data/raw/telecom_churn.csv"
)

print(f"Original Records: {len(df)}")

# Remove duplicates
df = df.drop_duplicates()

# Remove negative usage
df = df[df["data_used"] >= 0]

# Age Groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[18, 25, 35, 45, 60, 100],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-60",
        "60+"
    ]
)

# Salary Bands
df["salary_band"] = pd.cut(
    df["estimated_salary"],
    bins=[
        0,
        30000,
        60000,
        100000,
        999999999
    ],
    labels=[
        "0-30K",
        "30K-60K",
        "60K-100K",
        "100K+"
    ]
)

df.to_csv(
    "data/cleaned/telecom_clean.csv",
    index=False
)

print(
    f"Clean Records: {len(df)}"
)

print(
    "\nSaved -> data/cleaned/telecom_clean.csv"
)