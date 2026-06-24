import duckdb

conn = duckdb.connect(
    "data/warehouse/telecom.duckdb"
)

tables = conn.execute(
    "SHOW TABLES"
).fetchall()

print(tables)

conn.close()