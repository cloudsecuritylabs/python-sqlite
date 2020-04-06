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

# Select data from a table
cursor.execute("SELECT * from customers")

# get one, many or all
#print(cursor.fetchall())
#cursor.fetchmany(5)
#cursor.fetchone()

for row in cursor.fetchall():
    print(row)
    print(row[1] +" " + row[2] + " " + row[3])

# Using a where clause
cursor.execute("SELECT * from customers where last_name='Basu'")
print(cursor.fetchall())

cursor.execute("SELECT * from customers where email like ('%gmail%')")
for row in cursor.fetchall():
    #print(row)
    print(row[1] +" " + row[2] + " " + row[3])


# commit to database
conn.commit()

# close connection to the Database
conn.close()

