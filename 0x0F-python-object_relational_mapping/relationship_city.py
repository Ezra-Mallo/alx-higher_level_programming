#!/usr/bin/python3

"""My orm class"""

from sqlalchemy.orm import relationship
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import State, Base, relationship


class City(Base):
    """Cities class
    Attributes:
        __tablename__ (str) = The table name of the class
        id (int) = auto_increment and NOT nullable, PK
        name (str) =  The State name of the class
        state_id (str) =  The State id name of the state class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
