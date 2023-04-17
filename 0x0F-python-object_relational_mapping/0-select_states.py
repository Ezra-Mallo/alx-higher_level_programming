#!/usr/bin/python3

""" A script that lists all states from the database hbtn_0e_0_usa
   Your script should take 3 arguments: 
       mysql username,
       mysql password and
       database name (no argument validation needed)

   You must use the module MySQLdb (import MySQLdb)
   Script should connect to a MySQL server running on localhost at port 3306
   Results must be sorted in ascending order by states.id
   Results must be displayed as they are in the example below
   Your code should not be executed when imported"""

import sys
import MySQLdb

my_username = sys.argv[1]
my_password = sys.argv[2]
my_database = sys.argv[3]
my_port = 3306
my_host = "localhost"


if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connection = MySQLdb.connect(host=my_host,
                                    user=my_username,
                                    port=my_port,
                                    passwd=my_password,
                                    db=my_database)

    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM states")

    db_records_selected = db_cursor.fetchall()

    for record in db_records_selected:
        print(record)
