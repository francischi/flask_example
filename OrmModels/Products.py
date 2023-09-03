from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,ForeignKey
from marshmallow import Schema, fields
from .Categories import CategorySchema
from .Codes import CodeSchema
from .ProductSize import ProductSizeSchema
from .ProductColor import ProductColorSchema
import time

class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    unit_price = fields.Integer()
    inventory = fields.Integer()
    delete_time = fields.Integer()
    update_time = fields.Integer()
    create_time = fields.Integer()
    category = fields.Nested('CategorySchema')
    sizes = fields.List(fields.Nested('ProductSizeSchema'))
    colors = fields.List(fields.Nested('ProductColorSchema'))
    code = fields.Nested('CodeSchema')

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)

    name = Column(String(36), nullable=False)

    code_id = Column(Integer, ForeignKey('codes.id'), nullable=False)

    category_id = Column(Integer , ForeignKey('categories.id'), nullable=False)

    unit_price = Column(Integer, nullable=False)

    inventory = Column(Integer, nullable=False)

    create_time = Column(Integer, nullable=False)

    update_time = Column(Integer, nullable=True)

    delete_time = Column(Integer, nullable=True)

    category = relationship('Category',lazy="joined", back_populates='products')

    code = relationship('Code',lazy="joined", back_populates='products')

    sizes = relationship('Size', secondary='products_size', back_populates='products')

    colors = relationship('Color', secondary='products_color', back_populates='products')

    def __init__(self, name:str, code_id :int, category_id:int , unit_price:int ,inventory:int):
        create_time = int(time.time()) 
        self.name = name
        self.code_id = code_id
        self.category_id = category_id
        self.unit_price = unit_price
        self.inventory = inventory
        self.create_time = create_time

    def serialize(self):
        product_schema = ProductSchema()
        return product_schema.dump(self)