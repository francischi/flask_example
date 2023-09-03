from .Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String
from marshmallow import Schema, fields

class CodeSchema(Schema):
    id = fields.Integer()
    name = fields.String()

class Code(Base):
    __tablename__ = 'codes'
    
    id = Column(Integer, primary_key=True)

    name = Column(String(36), nullable=False)

    products = relationship("Product", back_populates='code')

    def __init__(self, name:str):
        self.name = name

    def serialize(self):
        code_schema = CodeSchema()
        return code_schema.dump(self)