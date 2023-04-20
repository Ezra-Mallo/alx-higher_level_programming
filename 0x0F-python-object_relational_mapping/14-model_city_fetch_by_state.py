#!/usr/bin/python3
"""This class makes reference to Base model of City)"""

from sys import argv
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    """Setting up the session engine"""
    if len(argv) <= 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        my_session = Session()
        my_query = my_session.query(City, State).join(State).order_by(City.id)

        for city, state in my_query:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
