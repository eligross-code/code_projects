### This is the main entrypoint for the app...

from ai_client import OpenAIClient
from database import Database
from database_config import tables
import database_config

# our runtime objects for the DB and AI service
# the database should reconnect if not already connected
database = Database("user_database.db", tables)
ai_client = OpenAIClient("gpt-5.5")

def startup() -> None:
    database.connect()
    database.create_tables()

    
def handle_event(raw_input):
    database.connect()
    database.create_tables(tables)
    database.insert_raw(raw_input)

    distilled = ai_client.call_ai(raw_input)["text"]
    database.insert_distilled(distilled)




def shutdown() -> None:
    database.close()

