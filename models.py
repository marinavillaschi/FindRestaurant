from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    restaurant_id = Column(Integer, primary_key = True)
    restaurant_name = Column(String, nullable = False)
    restaurant_address = Column(String)
    pic_url = Column(String)
    
    #Add add a decorator property to serialize data from the database
    @property
    def serialize(self):
        return {
        "id": self.restaurant_id,
        "restaurant_name": self.restaurant_name,
        "restaurant_address": self.restaurant_address,
        "image": self.pic_url}

engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine)