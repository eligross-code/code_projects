## We will set up a database, and create some basic write / read functions that we can reuse.
## The goal is to be modular, so this code can be reused in other projects.

"""
SQL core commands:

CREATE
INSERT
SELECT
UPDATE
DELETE
JOIN
WHERE
ORDER BY
GROUP BY

"""

import sqlite3

# create the database

database = sqlite3.connect('my_database.db')

# create a table
# id integer primary key creates a unique numeric id for each row --auto done
database.execute("""
                 CREATE TABLE IF NOT EXISTS notes (
                 id INTEGER PRIMARY KEY, 
                 text TEXT NOT NULL )


                 """)


# add something, the (?) is a placeholder for the value. This prevent SQL injection attacks, and is a best practice.

# values is used to denote the value of insertion.
database.execute(" INSERT INTO notes (text) VALUES (?)",
                 ("This is my first note",)
    )


# commit the changes to the database
database.commit()

# search for something
# fetchall returns a list of tuples, where there is the (row id, text) from the SELECT statement
# LIKE is searching using patterns
results = database.execute(
    "SELECT id, text FROM notes WHERE text LIKE ?", ("%This%",)
).fetchall()


# delete with condition
database.execute("DELETE FROM notes WHERE text LIKE ?", ("%first%",))
# need to commit changes, incuding deletions.
database.commit()

# finish off my closing the database
database.close()