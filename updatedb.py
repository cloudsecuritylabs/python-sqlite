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

# Update data into a table
cursor.execute("""
                  UPDATE customers 
                  SET first_name="UpdatedAnkan" 
                  WHERE id=1
        """
        )

conn.commit()


# Select data from a table
cursor.execute("SELECT * from customers WHERE id=1")

# get one, many or all
#print(cursor.fetchall())
#cursor.fetchmany(5)
#cursor.fetchone()

for row in cursor.fetchall():
    print(row)
    print(row[1] +" " + row[2] + " " + row[3])

# commit to database
conn.commit()

# close connection to the Database
conn.close()

