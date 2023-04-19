#!/usr/bin/python3
""" This script prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

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
    my_query = my_session.query(State).filter(State.name == sys.argv[4])


    if my_query.count() is None:
        print("Nothing found")
    else:
        for state in my_query.all():
            print("{}".format(state.id))
