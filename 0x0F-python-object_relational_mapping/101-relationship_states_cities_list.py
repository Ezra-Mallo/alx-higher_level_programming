#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, State
import sys


if __name__ == "__main__":
    db_engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                              format(argv[1], argv[2], argv[3]),
                              pool_pre_ping=True)
    Session = sessionmaker(bind=db_engine)
    my_session = Session()

    states = my_session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

        # because of the relationship between state and city table
        # we can get all the cities associated with a state
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
