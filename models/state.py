#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") != "db":
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref='state')
    else:
        @property
        def cities(self):
            """Get a list of all related City objects."""
            cities = list()
            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return cities