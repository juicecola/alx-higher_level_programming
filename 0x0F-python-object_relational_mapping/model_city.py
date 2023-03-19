#!/usr/bin/python3
""" model_city.py
    Python file similar to model_state.py
    named model_city.py that contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    """City class
    Args:
        Base (Object): Base class
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
