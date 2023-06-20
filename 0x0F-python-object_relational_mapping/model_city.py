#!/usr/bin/python3

"""My orm class"""

from sqlalchemy.orm import relationship
from model_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """Cities class
    Attributes:
        __tablename__ (str) = The table name of the class
        id (int) = auto_increment and NOT nullable, PK
        name (str) =  The State name of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
    
