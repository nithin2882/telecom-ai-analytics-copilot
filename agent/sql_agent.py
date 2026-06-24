import ollama
import duckdb

MODEL = "qwen3:4b"

conn = duckdb.connect(
    "data/warehouse/telecom.duckdb"
)

SCHEMA = """
Tables:

dim_customer(
customer_id,
gender,
age,
age_group,
num_dependents,
salary_band
)

fact_customer_usage(
customer_id,
telecom_partner,
state,
city,
pincode,
registration_date,
calls_made,
sms_sent,
data_used,
estimated_salary,
churn
)
"""

question = input(
    "\nAsk a business question: "
)

prompt = f"""
You are a Telecom SQL Expert.

Database Schema:

{SCHEMA}

Rules:
1. Return ONLY SQL
2. No explanation
3. Use DuckDB syntax

Question:
{question}
"""

response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

sql = response["message"]["content"]

print("\nGenerated SQL:\n")
print(sql)

try:

    result = conn.execute(sql).fetchdf()

    print("\nResult:\n")
    print(result)

except Exception as e:

    print("\nSQL Error:")
    print(e)

conn.close()