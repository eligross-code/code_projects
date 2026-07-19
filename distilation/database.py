### this is the database class, where the functions specific to the tables will be run
import sqlite3
from database_config import tables
class Database():
    def __init__(self, database: str):
        self.connection = False
        self.database_path = database
        self.database = None

        # these are the tables in the database_config
        self.tables_names = tables
        self.table1 = tables[0]
        self.table2 = tables[1]

    def connect(self) -> None:
        self.database = sqlite3.connect(self.database_path)
        self.connection = True


    # these rely off the tables in database_config. This should be more modular...
    def insert_raw(self, ai_response : str) -> None:
        # need to protect agaisnt prompt injection here too
        self.database.execute(
            
            "INSERT into raw_ai_convos (text) values (?)",
            "(ai_response,)",
    

        )
        # always connect changes
        self.database.commit()
    def insert_distilled(self, ai_summary : str) -> None:
              # need to protect agaisnt prompt injection here too
        self.database.execute(
            
            "INSERT into distilled_ai (text) values (?)",
            "(ai_response,)",
    

        )
        # always connect changes
        self.database.commit()

    