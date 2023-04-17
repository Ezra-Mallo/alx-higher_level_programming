#!/usr/bin/python3

""" A script that lists all states from the database hbtn_0e_0_usa
   Script takes 3 arguments(mysql username, mysql password & database name"""

from sys import argv
import MySQLdb

my_username = argv[1]
my_pswd = argv[2]
my_dbase = argv[3]
my_port = 3306
my_host = "localhost"

print(my_username, my_password, my_database)

"""    Connect to database, query and display states from the database."""
    data_base = MySQLdb.connect(user=my_username,passwd=my_pswd, db=my_dbase)

    db_cursor = data_base.cursor()
    data_base_cursor.execute("SELECT * FROM `states`")
    for state in  data_base_cursor.fetchall():
      print(record)
