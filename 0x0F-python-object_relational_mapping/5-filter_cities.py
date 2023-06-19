#!/usr/bin/python3

"""A script that takes in the name of a state as an argument and lists all
   cities of that state, using the database hbtn_0e_4_usa

    * Your script should take 4 arguments: mysql username, mysql password,
      database name and state name (SQL injection free!)
    * You must use the module MySQLdb (import MySQLdb)
    * Your script should connect to a MySQL server running on localhost at
      port 3306
    * Results must be sorted in ascending order by cities.id
    * You can use only execute() once
    * The results must be displayed as they are in the example below
    * Your code should not be executed when importedscript that lists all
      cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """    Connect to database, query and display states from the database."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], database=argv[3])
    db_cursor = db.cursor()
    my_query = "SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id"
    my_search = argv[4]

    db_cursor.execute(my_query, (my_search, ))
    result = db_cursor.fetchall()

    my_list = []

    for cities in result:
        my_list.append(cities[0])
    print(my_list)

    db_cursor.close()
    db.close()
