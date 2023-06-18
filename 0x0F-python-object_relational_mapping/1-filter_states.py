#!/usr/bin/python3

"""A script that lists all states with a name starting with N (upper N) from
   the database hbtn_0e_0_usa:
    Your script should take 3 arguments: mysql username, mysql password and
    database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port
    3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """    Connect to database, query and display states from the database."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], database=argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM `states` WHERE name LIKE BINARY 'N%'\
                      ORDER BY id")
    for state in db_cursor.fetchall():
        print(state)
    for state in db_cursor.fetchall():
        print(state)
