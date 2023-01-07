#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    """ The city class, contains state ID and name 
    
    Inherits from SQLALchemy Base class, and models the Cities table
    on the DBstorage
    
    Attributes:
        __tablename__ (str): the name of the MySQL table the class models, Cities
        name (sqlalchemy String): the id of a city model from the table - a row
        state_id (sqlalchemy String): the id of the state the city belongs to
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
