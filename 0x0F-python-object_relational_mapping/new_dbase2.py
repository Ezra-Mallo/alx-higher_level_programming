#!/usr/bin/python3

from sqlalchemy import create_engine
from sys import argv

# Establish a connection to the MySQL server
connection_string = 'mysql+mysqldb://root:root@localhost'
db_engine = create_engine(connection_string, pool_pre_ping=True)

# Create a connection from the engine
db_connection = db_engine.connect()

# Create the database
db_connection.execute('CREATE DATABASE IF NOT EXISTS library2')

# Close the connection
db_connection.close()
db_engine.dispose()
