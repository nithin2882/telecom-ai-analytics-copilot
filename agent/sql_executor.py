import duckdb

DB_PATH = "data/warehouse/telecom.duckdb"


class SQLExecutor:

    def __init__(self):
        self.conn = duckdb.connect(DB_PATH)

    def execute(self, sql):
        return self.conn.execute(sql).fetchdf()

    def close(self):
        self.conn.close()