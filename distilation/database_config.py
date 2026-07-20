### Set up datbase, basic schema for distillation data and raw events, insert and query functions.
import sqlite3

# connect or make the db
user_database = sqlite3.connect(
    "database.db"
)


# USE DEFAULT CURRENT_TIMESTAMP to automatically capture current time 

# 2026-07-19 16:30:00 is the format
tables = ["""
                CREATE TABLE IF NOT EXISTS raw_ai_convos (
                 id INTEGER PRIMARY KEY, 
                 text TEXT NOT NULL,
                 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP ) """,
                  
          """
                 CREATE TABLE IF NOT EXISTS distilled_ai (
                 id INTEGER PRIMARY KEY, 
                 text TEXT NOT NULL,
                 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP )

                                    """]
for table in tables:
    user_database.execute(table)

user_database.commit()

