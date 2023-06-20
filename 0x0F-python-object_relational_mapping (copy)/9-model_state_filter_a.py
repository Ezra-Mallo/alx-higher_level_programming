#!/usr/bin/python3
""" This script calls the object Base state and makes a session to
query the Base classi to dislay first record. It wgrk with MySQLAlchemy ORM."""

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
    my_query = my_session.query(State).filter(State.name
                                              .like('%a%')).order_by(State.id)

    for state in my_query.all():
        print("{}: {}".format(state.id, state.name))
