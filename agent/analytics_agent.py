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

sql_prompt = f"""
You are a Telecom SQL Expert.

Schema:

{SCHEMA}

Return ONLY SQL.

Question:
{question}
"""

sql_response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": sql_prompt
        }
    ]
)

sql = sql_response["message"]["content"]

sql = sql.replace("```sql", "")
sql = sql.replace("```", "")
sql = sql.strip()

print("\nGenerated SQL:\n")
print(sql)

df = conn.execute(sql).fetchdf()

print("\nResult:\n")
print(df)

insight_prompt = f"""
You are a Telecom Business Analyst.

Question:
{question}

Result:
{df.to_string(index=False)}

Provide:
1. Key finding
2. Business impact
3. Recommended action

Keep it concise.
"""

insight = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": insight_prompt
        }
    ]
)

print("\nBusiness Insight:\n")
print(
    insight["message"]["content"]
)

conn.close()