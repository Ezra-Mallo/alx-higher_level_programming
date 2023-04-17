#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N)
   Script takes 3 arguments(mysql username, mysql password & database name
   from the database hbtn_0e_0_usa:"""

from sys import argv
import MySQLdb

my_user = argv[1]
my_pswd = argv[2]
my_db = argv[3]
my_port = 3306
my_host = "localhost"

if __name__ == "__main__":
    """    Connect to database, query and display states from the database."""
    db = MySQLdb.connect(host=my_host, port=my_port,
                         user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    for state in db_cursor.fetchall():
        print(state)
