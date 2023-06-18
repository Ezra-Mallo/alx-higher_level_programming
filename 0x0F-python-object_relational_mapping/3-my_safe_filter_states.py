#!/usr/bin/python3

"""A script that takes in arguments and displays all values in the states
     table of hbtn_0e_0_usa where name matches the argument. But this time,
     write one that is safe from MySQL injections!

    * Your script should take 4 arguments: mysql username, mysql password,
      database name and state name searched (safe from MySQL injection)
    * You must use the module MySQLdb (import MySQLdb)
    * Your script should connect to a MySQL server running on localhost at
      port 3306
    * Results must be sorted in ascending order by states.id
    * Results must be displayed as they are in the example below
    * Your code should not be executed when imported"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """    Connect to database, query and display states from the database."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], database=argv[3])
    db_cursor = db.cursor()
    query = "SELECT * FROM `states` WHERE name = %s"
    arg_value = argv[4]
    db_cursor.execute(query, (arg_value, ))
    result = db_cursor.fetchall()
    for state in result:
        print(state)

    db_cursor.close()
    db.close()
