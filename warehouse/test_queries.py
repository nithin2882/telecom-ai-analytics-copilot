import duckdb

conn = duckdb.connect(
    "data/warehouse/telecom.duckdb"
)

print("\nTotal Customers")

print(
    conn.execute(
        """
        SELECT COUNT(*)
        FROM dim_customer
        """
    ).fetchall()
)

print("\nChurn Rate")

print(
    conn.execute(
        """
        SELECT
            ROUND(
                AVG(churn) * 100,
                2
            ) AS churn_rate
        FROM fact_customer_usage
        """
    ).fetchall()
)

print("\nTop 5 States By Customers")

print(
    conn.execute(
        """
        SELECT
            state,
            COUNT(*) customers
        FROM fact_customer_usage
        GROUP BY state
        ORDER BY customers DESC
        LIMIT 5
        """
    ).fetchdf()
)

conn.close()