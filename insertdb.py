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

# Insert data into a table
cursor.execute("""INSERT INTO customers (first_name, last_name, email) VALUES(
        "Ankan",
        "Basu",
        "basu.ankan@gmail.com"
        )
        """
        )

cursor.execute("""INSERT INTO customers (first_name, last_name, email) VALUES(
        "Sovon",
        "Samanta",
        "samanta@hotmail.com"
        )
        """
        )

cursor.execute("""INSERT INTO customers (first_name, last_name, email) VALUES(
        "Chandan",
        "Addya",
        "chandan@gmail.com"
        )
        """
        )

# Make a list of customers to insert into the database
customer_list = [
    ("Black" , "Hat", "Black@gmail.com"),
    ("White" , "Hat", "white@gmail.com"),
    ("Grey" , "Hat", "Grey@gmail.com"),
    ("Green" , "Cap", "Grey@yahoo.com"),
    ("Yellow" , "Cap", "yello@gmail.com"),
    ("Orange" , "Cap", "orange@yahoo.com"),
    ("Blue" , "Cap", "blue@yahoo.com"),
    ("Purple" , "Cap", "purple@gmail.com"),
    ("Brown" , "Pal", "brown@outlook.com"),
    ("Pink" , "Gal", "Pink@outlook.com"),
    ("Maroon" , "Gal", "Maroon@gmail.com"),
    ("Light" , "Blue", "Light@blue.com"),
    ("Dark" , "Blue", "Dark@gblue.com"),
    ("Dark" , "Brown", "dark@brown.com")
]

# no need to write a loop!
cursor.executemany("INSERT INTO customers (first_name, last_name, email) VALUES(?,?,?)", customer_list)

# commit to database
conn.commit()

# Select data from a table to see if everything is ok
cursor.execute("SELECT * from customers")
for row in cursor.fetchall():
    #print(row)
    print(row[1] +" " + row[2] + " " + row[3])

conn.commit()

# close connection to the Database
conn.close()

