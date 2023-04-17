#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=db_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Prepare the SQL query with a parameterized query to prevent SQL injection attacks
    query = "SELECT * FROM states WHERE name = %s"

    # Execute the SQL query with the state_name argument as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the database connection
    db.close()
