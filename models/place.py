#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay

    Inherits from SQLAlchemy Base and link to the MySQL table places.
    Attributes:
        __tablename__ (str): the name of the linked to, and
                             used to store instances of the class
        city_id (sqlalchemy String): place's city id
        user_id (sqlalchemy String): place's lister/user id
        name (sqlalchemy String): the name of the place
        description (sqlalchemy String): description of the place
        number_room (sqlalchemy Integer): number of rooms in the place
        number_bathrooms (sqlalchemy Integer): number of bathrooms in the place
        max_guest (sqllchemy Integer): max number of quest the place can hold
        price_by_night (sqlalchemy Integer): the price per night
        latitude (sqlalchemy Float): the place's latitude - co-ordinates
        longitude (sqlalchemy Float): the place's langitude - co-ordinate
        amenity_ids (list): list of available amenities in the place
        """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Returns a list of all the reviews associated with the place"""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.place_id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Returns a list of all availables amenities in a place"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
