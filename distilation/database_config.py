### Set up datbase, basic schema for distillation data and raw events, insert and query functions.
import sqlite3

# connect or make the db
user_database = sqlite3.connect(
    "database.db"
)

tables = ["""
                CREATE TABLE IF NOT EXISTS raw_ai_convos (
                 id INTEGER PRIMARY KEY, 
                 text TEXT NOT NULL ) """,
                  
          """
                 CREATE TABLE IF NOT EXISTS distilled_ai (
                 id INTEGER PRIMARY KEY, 
                 text TEXT NOT NULL )

                                    """]
for table in tables:
    user_database.execute(table)

user_database.commit()

