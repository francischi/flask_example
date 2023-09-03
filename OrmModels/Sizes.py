from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String
from marshmallow import Schema, fields

class SizeSchema(Schema):
    id = fields.Integer()
    name = fields.String()

class Size(Base):
    __tablename__ = 'sizes'

    id = Column(Integer , primary_key=True)

    name = Column(String(36), nullable=False)

    products = relationship('Product', secondary='products_size', back_populates='sizes')

    def __init__(self, name:str):
        self.name = name