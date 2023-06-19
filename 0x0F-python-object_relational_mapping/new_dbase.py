#!/usr/bin/python3
# sudo <./filename> <username> <password> <dbase name>
# sudo ./new_dbase root root library_db

from sys import argv
import MySQLdb


# Establish a connection to the MySQL server
db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2])

# Create a cursor object to execute SQL statements
cursor = db.cursor()

# Create the "Library" database
my_query = ("CREATE DATABASE {}".format(argv[3]))
cursor.execute(my_query)

# Close the cursor and database connection
cursor.close()
db.close()
