### This is the main entrypoint for the app...

from ai_client import OpenAIClient
from database import Database
from database_config import tables
import database_config

def main(raw_input):
    # our runtime objects for the DB and AI service
    # the database should reconnect if not already connected
    database = Database("user_database.db", tables)
    ai_client = OpenAIClient("gpt-5.5")


    # first add the the raw_convo to the DB
    database.connect()
    database.create_tables(tables)
    database.insert_raw(raw_input)
    


