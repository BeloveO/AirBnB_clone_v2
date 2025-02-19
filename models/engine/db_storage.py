#!/usr/bin/python3

from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    New engine for storage using sql
    """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        my_dict = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                my_dict[key] = elem
        else:
            a_list = [State, City, User, Place, Amenity, Review]
            for a in a_list:
                query = self.__session.query(a)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    my_dict[key] = elem
        return (my_dict)

    def new(self, obj):
        """
        Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        Create the current database session
        """
        Base.metadata.create_all(self.__engine)
        cur_sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(cur_sess)
        self.__session = Session()

    def close(self):
        """
        Close the working session
        """
        self.__session.close()
