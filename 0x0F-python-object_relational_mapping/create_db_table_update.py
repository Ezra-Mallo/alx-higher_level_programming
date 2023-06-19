#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for declarative models
Base = declarative_base()

# Create the database engine
db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
#db_engine = create_engine('sqlite:///library4.db', echo=True)
Base.metadata.create_all(db_engine)
    
    
# Create a session
Session = sessionmaker(bind=db_engine)
db_session = Session()


# Define the Book model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    bk_name = Column(String(255), nullable=False)
    publisher = Column(String(255), nullable=False)
    yr = Column(Integer, nullable=False)

# Define the Author model
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

# Define the Borrow model
class Borrow(Base):
    __tablename__ = 'borrow'

    id = Column(Integer, primary_key=True)
    book = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)

# Define the Staff model
class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    dept = Column(String(255), nullable=False)

# Create the database tables
Base.metadata.create_all(db_engine)

# Insert values into the tables
book1 = Book(bk_name='Book 1', publisher='Publisher 1', yr=2022)
book2 = Book(bk_name='Book 2', publisher='Publisher 2', yr=2021)

author1 = Author(name='Author 1')
author2 = Author(name='Author 2')

borrow1 = Borrow(book=1, student_id=1)
borrow2 = Borrow(book=2, student_id=2)

staff1 = Staff(name='Staff 1', password='password1', dept='Dept 1')
staff2 = Staff(name='Staff 2', password='password2', dept='Dept 2')

db_session.add_all([book1, book2, author1, author2, borrow1, borrow2, staff1, staff2])
db_session.commit()

# Close the 
db_session.close()

