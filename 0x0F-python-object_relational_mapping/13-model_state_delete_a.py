#!/usr/bin/python3
"""A script that deletes all State objects with a name containing the letter
   a from the database hbtn_0e_6_usa

   * Your script should take 3 arguments: mysql username, mysql password and
     database name
   * You must use the module SQLAlchemy
   * You must import State and Base from model_state - from model_state
     import Base, State
   * Your script should connect to a MySQL server running on localhost at
     port 3306
   * Your code should not be executed when imported
"""
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

    my_query = my_session.query(State).filter(State.name.like('%a%')).all()

    if my_query:
        # delete query
        for state in my_query:
            my_session.delete(state)
        my_session.commit()

    my_session.close()
    db_engine.dispose()
