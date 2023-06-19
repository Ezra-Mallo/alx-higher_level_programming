#!/usr/bin/python3

"""A script that lists all cities from the database hbtn_0e_4_usa

    * Your script should take 3 arguments: mysql username, mysql password and
    database name
    * You must use the module MySQLdb (import MySQLdb)
    * Your script should connect to a MySQL server running on localhost at
    port 3306
    * Results must be sorted in ascending order by cities.id
    * You can use only execute() once
    * Results must be displayed as they are in the example below
    * Your code should not be executed when imported
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """    Connect to database, query and display states from the database."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], database=argv[3])
    db_cursor = db.cursor()
    query = "SELECT a.id, a.name, b.name\
            FROM `cities` as a\
            INNER JOIN states as b\
            ON a.state_id = b.id\
            ORDER BY a.id ASC"

    db_cursor.execute(query)
    result = db_cursor.fetchall()
    for cities in result:
        print(cities)

    db_cursor.close()
    db.close()
