#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument.
   Script takes 3 arguments(mysql username, mysql password & database name"""

from sys import argv
import MySQLdb

my_user = argv[1]
my_pswd = argv[2]
my_db = argv[3]
my_match = argv[4]
my_port = 3306
my_host = "localhost"

if __name__ == "__main__":
    db = MySQLdb.connect(host=my_host, port=my_port,
                         user=my_user, passwd=my_pswd, db=my_db)
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name = '{}'".format(my_match))

    for state in db_cursor.fetchall():
        print(state)
