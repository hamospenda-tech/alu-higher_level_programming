#!/usr/bin/python3
"""Contains the class definition of a City"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (int): the city's id, primary key.
        name (str): the city's name.
        state_id (int): the id of the state the city belongs to.
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
