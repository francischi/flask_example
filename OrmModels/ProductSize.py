from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,ForeignKey
from marshmallow import Schema, fields
from .Sizes import SizeSchema

class ProductSizeSchema(Schema):
    size = fields.Nested(SizeSchema)
    name = fields.String()

class ProductSize(Base):
    __tablename__ = 'products_size'

    id = Column(Integer , primary_key=True)

    product_id = Column(Integer , ForeignKey('products.id') , nullable=False)

    size_id = Column(Integer , ForeignKey('sizes.id') , nullable=False)

    def __init__(self, product_id:int, size_id:int):
        self.product_id = product_id
        self.size_id = size_id