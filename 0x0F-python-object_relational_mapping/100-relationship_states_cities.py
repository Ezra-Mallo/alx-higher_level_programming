#!/usr/bin/python3
"""elationship model"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base


if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(db_engine)

    Session = sessionmaker(bind=db_engine)
    my_session = Session()

    new_city = City(name='San Francisco')
    new_state = State(name='California')
    state.cities.append(new_city)
    my_session.add(new_state)
    my_session.add(new_city)
    my_session.commit()

    my_session.close()
    db_engine.dispose()
