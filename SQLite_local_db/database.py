### wrapper over some SQlite commands to make it easier to use. This is a modular code that can be reused in other projects.
import sqlite3

# class wrapper
class Database():
    def __init__(self, db_name):
        self.db_name = db_name
        self.database = None

    # Simple functions
    def connect(self):
        self.database = sqlite3.connect(self.db_name)

    def commit(self):
        self.database.commit()

    def close(self):
        self.database.close()

   
    def execute(self, sql: str, values: tuple = ()):
        if self.connection is None:
            raise RuntimeError("Database is not connected.")

        return self.connection.execute(sql, values)
    

    # potentially more specific functions
    def search_notes(self, search_text: str):
        return self.execute(
            "SELECT id, text FROM notes WHERE text LIKE ?",
            (f"%{search_text}%",)
        ).fetchall()