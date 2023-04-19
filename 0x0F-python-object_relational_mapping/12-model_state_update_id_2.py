#!/usr/bin/python3
""" This script adds the State object “Louisiana” to the database
hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    my_session = Session()
    my_query = my_session.query(State).filter(State.id == 2)

    if my_query.count() != 0:
        for state in my_query:
            state.name = "New Mexico"
            my_session.commit()
