#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument.
   Script takes 3 arguments(mysql username, mysql password & database name"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """    Connect to database, query and display states from the database."""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states\
                      WHERE name = '{}'".format(argv[4]))
    for state in db_cursor.fetchall():
        print(state)
