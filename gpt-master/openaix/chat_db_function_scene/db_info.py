import sqlite3

class DbInfo:

    def get_conn(self):
        conn = sqlite3.connect("./chinook.db")
        return conn

    def get_table_names(self):
        table_names = []
        tables = self.get_conn().execute("SELECT name FROM sqlite_master WHERE type='table';")
        for table in tables.fetchall():
            table_names.append(table[0])
        return table_names

    def get_column_names(self,table_name):
        column_names = []
        columns = self.get_conn().execute(f"PRAGMA table_info('{table_name}');").fetchall()
        for col in columns:
            column_names.append(col[1])
        return column_names

    def get_database_info(self):
        table_dicts = []
        for table_name in self.get_table_names():
            columns_names = self.get_column_names(table_name)
            table_dicts.append({"table_name": table_name, "column_names": columns_names})
        return table_dicts

    def get_sqlite_db_info(self):
        database_schema_dict = self.get_database_info()
        database_schema_string = "\n".join(
            [
                f"Table: {table['table_name']}\nColumns: {', '.join(table['column_names'])}"
                for table in database_schema_dict
            ]
        )
        return database_schema_string

if __name__ == '__main__':
    db_info = DbInfo()
    sqllite_infos = db_info.get_sqlite_db_info()
    print(sqllite_infos)