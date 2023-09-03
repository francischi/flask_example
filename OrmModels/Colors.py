from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String
from marshmallow import Schema, fields

class ColorSchema(Schema):
    id = fields.Integer()
    name = fields.String()

class Color(Base):
    __tablename__ = 'colors'

    id = Column(Integer , primary_key=True)

    name = Column(String(36), nullable=False)

    products = relationship('Product', secondary='products_color', back_populates='colors')

    def __init__(self, name:str):
        self.name = name