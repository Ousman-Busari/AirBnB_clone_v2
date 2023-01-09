#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes

    Inherits from SQLAlchmey Base class and links to the users table on MySQL

    Attributes:
        __table__name (str): the name of the table the class models it rows
        email (sqlalchemy String): email address of a user
        password (sqlalchemy String): the password of the user
        first_name (sqlalchemy String): user first name
        last_name (sqlalchemy String): user last name
        places (sqlalchmey relationship): relates a user all places listed
                                          under it
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
