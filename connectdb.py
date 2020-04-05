# Author: Ankan Basu
# import the database module
import sqlite3

# connect to a database
conn = sqlite3.connect('tutorialcustomer.db')

# to connect to a database in memory
# conn = sqlite3.connect(':memory:')

# Create a custor to work with the database
cursor = conn.cursor()
#cursor.execute("DROP TABLE customers")

#create a table
cursor.execute("""CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT
        )
        """
        )
        
# commit to database
conn.commit()

# close connection to the Database
conn.close()
