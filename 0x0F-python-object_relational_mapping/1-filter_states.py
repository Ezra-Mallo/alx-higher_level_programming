#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N)
   Results must be sorted in ascending order by states.id
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
    db = MySQLdb.connect(host=my_host, port=my_port,
                         user=my_user, passwd=my_pswd, db=my_db)
    db_cursor = db.cursor()
    # db_cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    db_cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in db_cursor.fetchall() if state[1][0] == "N"]



"""    for state in db_cursor.fetchall():
        print(state)"""
