#!/usr/bin/python3
"""Start link class to table in database """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(db_engine)

    Session = sessionmaker(bind=db_engine)
    my_session = Session()

    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    my_session.close()
    db_engine.dispose()
