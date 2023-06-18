#!/usr/bin/python3

"""A script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument.
   
    *Your script should take 4 arguments: mysql username, mysql password,
      database name and state name searched (no argument validation needed)
    *You must use the module MySQLdb (import MySQLdb)
    *Your script should connect to a MySQL server running on localhost at port
     3306
    *You must use format to create the SQL query with the user input
    *Results must be sorted in ascending order by states.id
    *Results must be displayed as they are in the example below
    *Your code should not be executed when imported"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """    Connect to database, query and display states from the database."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], database=argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM `states` WHERE BINARY name ='{}'\
                      ORDER BY id".format(argv[4]))
    for state in db_cursor.fetchall():
        print(state)
    for state in db_cursor.fetchall():
        print(state)
