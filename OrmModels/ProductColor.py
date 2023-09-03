from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,ForeignKey
from marshmallow import Schema, fields
from .Colors import ColorSchema

class ProductColorSchema(Schema):
    size = fields.Nested(ColorSchema)
    name = fields.String()

class ProductColor(Base):
    __tablename__ = 'products_color'

    id = Column(Integer , primary_key=True)

    product_id = Column(Integer , ForeignKey('products.id') , nullable=False)

    color_id = Column(Integer , ForeignKey('colors.id') , nullable=False)

    def __init__(self, product_id:int, color_id:int):
        self.product_id = product_id
        self.color_id = color_id