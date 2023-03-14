import sqlite3


class DBAgent:

    @staticmethod
    def query_database(database: str, db_query: str, params: tuple = None):
        try:
            with sqlite3.connect(database) as db_connection:
                db_cursor = db_connection.cursor()
                if params:
                    content = db_cursor.execute(db_query, params)
                else:
                    content = db_cursor.execute(db_query)
        except Exception:
            return None
        return content
