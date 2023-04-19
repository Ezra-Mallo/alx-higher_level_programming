#!/usr/bin/python3
"""This class makes reference to Base model of City)"""

from sys import argv
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    """Setting up the session engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    my_session = Session()
    my_query = my_session.query(City)

    for cities in my_query.all():
        print(cities.id, cities.state_id, cities.name)
