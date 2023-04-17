#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument.
   Script takes 3 arguments(mysql username, mysql password & database name"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    my_search = argv[4]
    db_cursor = db.cursor()
    my_query = "SELECT * FROM states WHERE name = %s"

    db_cursor.execute(my_query, (my_search, ))
    for state in db_cursor.fetchall():
        print(state)
    db.close()
