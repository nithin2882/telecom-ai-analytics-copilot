import duckdb

conn = duckdb.connect(
    "data/warehouse/telecom.duckdb"
)

# Customer Dimension
conn.execute("""
CREATE OR REPLACE TABLE dim_customer AS
SELECT DISTINCT
    customer_id,
    gender,
    age,
    age_group,
    num_dependents,
    salary_band
FROM read_csv_auto(
    'data/cleaned/telecom_clean.csv'
)
""")

# Partner Dimension
conn.execute("""
CREATE OR REPLACE TABLE dim_partner AS
SELECT DISTINCT
    telecom_partner
FROM read_csv_auto(
    'data/cleaned/telecom_clean.csv'
)
""")

# Location Dimension
conn.execute("""
CREATE OR REPLACE TABLE dim_location AS
SELECT DISTINCT
    state,
    city,
    pincode
FROM read_csv_auto(
    'data/cleaned/telecom_clean.csv'
)
""")

# Date Dimension
conn.execute("""
CREATE OR REPLACE TABLE dim_date AS
SELECT DISTINCT
    CAST(date_of_registration AS DATE) as registration_date,
    YEAR(CAST(date_of_registration AS DATE)) as year,
    MONTH(CAST(date_of_registration AS DATE)) as month
FROM read_csv_auto(
    'data/cleaned/telecom_clean.csv'
)
""")

# Fact Table
conn.execute("""
CREATE OR REPLACE TABLE fact_customer_usage AS
SELECT
    customer_id,
    telecom_partner,
    state,
    city,
    pincode,
    CAST(date_of_registration AS DATE) as registration_date,
    calls_made,
    sms_sent,
    data_used,
    estimated_salary,
    churn
FROM read_csv_auto(
    'data/cleaned/telecom_clean.csv'
)
""")

print("Warehouse Created Successfully")

conn.close()
