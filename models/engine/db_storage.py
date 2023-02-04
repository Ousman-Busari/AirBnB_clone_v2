#!/usr/bin/python3
"""DBStorage engine definition - abstraction"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """class definition of the db storage

    Attributes:
        __engine (sqlalchemy engine): the created database engine
        __session (sqlalchemy session): the current session working
                                        on the engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialize a new instance of DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                        getenv("HBNB_MYSQL_USER"),
                                        getenv("HBNB_MYSQL_PWD"),
                                        getenv("HBNB_MYSQL_HOST"),
                                        getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current database session all objects of the given class

        If query is None, query all objects

        Return:
            DIct of queried class in the format <class nane>.<obj.id> = obj
        """

        if cls is None:
            objs_list = self.__session.query(State).all()
            objs_list.extend(self.__session.query(City).all())
            objs_lit.extend(self.__session.query(Place).all())
            objs_list.extend(self.__session.query(Amenity).all())
            objs_list.extend(self.__session.query(Review).all())
            objs_list.extend(self.__session.query(User).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs_list = self.__session.query(cls)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj
                for obj in objs_list}

    def new(self, obj):
        """Adds obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database, and a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ closes the session connection by remving the session scope """
        self.__session.remove()
