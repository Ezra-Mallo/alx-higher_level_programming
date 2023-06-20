#!/usr/bin/python3

""" A script that lists all states from the database hbtn_0e_0_usa
   Script takes 3 arguments(mysql username, mysql password & database name"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """    Connect to database, query and display states from the database."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM `states`")
    for state in db_cursor.fetchall():
        print(state)
