import duckdb

conn = duckdb.connect(
    "data/warehouse/telecom.duckdb"
)

queries = {

    "Total Customers":
    """
    SELECT COUNT(*)
    FROM dim_customer
    """,

    "Churn Rate":
    """
    SELECT ROUND(AVG(churn)*100,2)
    FROM fact_customer_usage
    """,

    "Average Data Usage":
    """
    SELECT ROUND(AVG(data_used),2)
    FROM fact_customer_usage
    """,

    "Top Telecom Partner":
    """
    SELECT
        telecom_partner,
        COUNT(*) customers
    FROM fact_customer_usage
    GROUP BY telecom_partner
    ORDER BY customers DESC
    LIMIT 1
    """,

    "Highest Churn Partner":
    """
    SELECT
        telecom_partner,
        ROUND(AVG(churn)*100,2) churn_rate
    FROM fact_customer_usage
    GROUP BY telecom_partner
    ORDER BY churn_rate DESC
    LIMIT 1
    """
}

for name, query in queries.items():

    print("\n" + "="*50)
    print(name)
    print("="*50)

    print(
        conn.execute(query).fetchall()
    )

conn.close()