#!/usr/bin/python3
"""A script that adds the State object “Louisiana” to the database
   hbtn_0e_6_usa

   * Your script should take 3 arguments: mysql username, mysql password and
     database name
   * You must use the module SQLAlchemy
   * You must import State and Base from model_state - from model_state import
     Base, State
   * Your script should connect to a MySQL server running on localhost at port
     3306
   * Print the new states.id after creation
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

    new_state = State(name='Louisiana')
    my_session.add_all([new_state])
    my_session.commit()

    print("{}".format(new_state.id))

    my_session.close()
    db_engine.dispose()
