#!/usr/bin/python3
"""A script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    Write one that is safe from MySQL injections!
   Script takes 3 arguments(mysql username, mysql password & database name"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    my_search = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db.cursor()
    my_query = "SELECT cities.name\
            FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %s\
            ORDER BY cities.id"
    db_cursor.execute(my_query, (my_search, ))
    result = list(db_cursor.fetchall())
    count = len(result)
    i = 1
    for cities in result:
        if (i < count):
            print(cities[0], end=", ")
        else:
            print(cities[0])
        i += 1


