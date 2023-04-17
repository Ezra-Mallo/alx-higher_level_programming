#!/usr/bin/python3
"""A script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    Write one that is safe from MySQL injections!
   Script takes 3 arguments(mysql username, mysql password & database name"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name\
                      FROM cities\
                      INNER JOIN states\
                      ON cities.state_id = states.id\
                      ORDER BY cities.id ASC")
    for state in db_cursor.fetchall():
        print(state)
    db.close()
