### this is the database class, where the functions specific to the tables will be run

import sqlite3
from database_config import tables

class Database():
    def __init__(self, database: str, tables):
    
        self.database_path = database
        self.database = None

        # a bit redunant since self.database already tells us
        self.connection = False

        # these are the tables in the database_config
        self.tables_names = tables


    def connect(self) -> None:
        self.database = sqlite3.connect(self.database_path)
        self.connection = True

    def create_tables(self, tables : list[str]) -> None:
        if self.database is None:
            raise RuntimeError("Call .connect() before creating tables")
        
        # create the tables
        for table in tables:
            self.database.execute()

    # always connect changes
        self.database.commit()


    # these rely off the tables in database_config. This should be more modular...
    def insert_raw(self, ai_response : str) -> None:
        # need to protect agaisnt prompt injection here too

        # need to be connected 
        if self.database is None:
            raise RuntimeError("Database is not connected. Call connect() first.")

        self.database.execute(
            
            "INSERT into raw_ai_convos (text) values (?)",
            (ai_response,),
    

        )
        # always connect changes
        self.database.commit()
    def insert_distilled(self, ai_summary : str) -> None:
        # need to protect agaisnt prompt injection here too

        # need to be connected 
        if self.database is None:
            raise RuntimeError("Database is not connected. Call connect() first.")  
          
        self.database.execute(
            
            "INSERT into distilled_ai (text) values (?)",
            (ai_summary,),
    

        )
        # always connect changes
        self.database.commit()

    # close the db
    def close(self) -> None:
        if self.database is not None:
            self.database.close()
            self.database = None
            self.connection = False        