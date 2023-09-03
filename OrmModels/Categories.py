from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String
from marshmallow import Schema, fields

class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.String()

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)

    name = Column(String(36), nullable=False)

    products = relationship("Product", back_populates='category')

    def __init__(self, name:str):
        self.name = name

    def serialize(self):
        category_schema = CategorySchema()
        return category_schema.dump(self)