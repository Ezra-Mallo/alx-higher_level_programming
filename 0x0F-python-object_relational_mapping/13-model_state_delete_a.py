#!/usr/bin/python3
"""This script deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    my_session = Session()
    my_query = my_session.query(State).filter(State.name.like('%a%'))
    if my_query.count() >= 1:
        my_query.delete()
    my_session.commit()
    my_session.close()