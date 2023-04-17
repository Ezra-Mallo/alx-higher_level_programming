#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N)
   Results must be sorted in ascending order by states.id
   Script takes 3 arguments(mysql username, mysql password & database name
   from the database hbtn_0e_0_usa:"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    for state in db_cursor.fetchall():
        print(state)
