#!/usr/bin/python3
"""A script that changes the name of a State object from the database
   hbtn_0e_6_usa

   * Your script should take 3 arguments: mysql username, mysql password
     and database name
   * You must use the module SQLAlchemy
   * You must import State and Base from model_state - from model_state
     import Base, State
   * Your script should connect to a MySQL server running on localhost at port
     3306
   * Change the name of the State where id = 2 to New Mexico
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

    my_query = my_session.query(State).filter(State.id == 2)
    if my_query.count() != 0:
        for state in my_query:
            state.name = "New Mexico"
            my_session.commit()

    my_session.commit()

    my_session.close()
    db_engine.dispose()
