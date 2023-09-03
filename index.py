from flask import Flask
from router import allRoute
from sqlalchemy import create_engine , inspect
import configparser
from OrmModels.Base import Base
from OrmModels import DB ,Products ,  Categories , Codes , Colors , ProductSize , ProductColor ,Sizes

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.register_blueprint(allRoute, url_prefix="/api")

# create table & migrate

if not inspect(DB.engine).has_table(Colors.Color.__tablename__):
    Colors.Color.__table__.create(bind = DB.engine)
    red = Colors.Color(name="red")
    blue = Colors.Color(name="blue")
    DB.session.add(red)
    DB.session.add(blue)
    DB.session.commit()

if not inspect(DB.engine).has_table(Categories.Category.__tablename__):
    Categories.Category.__table__.create(bind = DB.engine)
    cloth = Categories.Category(name="cloth")
    pants = Categories.Category(name="pants")
    DB.session.add(cloth)
    DB.session.add(pants)
    DB.session.commit()

if not inspect(DB.engine).has_table(Codes.Code.__tablename__):
    Codes.Code.__table__.create(bind = DB.engine)
    A = Codes.Code(name="A-001")
    B = Codes.Code(name="B-001")
    DB.session.add(A)
    DB.session.add(B)
    DB.session.commit()

if not inspect(DB.engine).has_table(Products.Product.__tablename__):
    Products.Product.__table__.create(bind = DB.engine)

if not inspect(DB.engine).has_table(Sizes.Size.__tablename__):
    Sizes.Size.__table__.create(bind = DB.engine)
    L = Sizes.Size(name="L")
    M = Sizes.Size(name="M")
    DB.session.add(L)
    DB.session.add(M)
    DB.session.commit()

if not inspect(DB.engine).has_table(ProductSize.ProductSize.__tablename__):
    ProductSize.ProductSize.__table__.create(bind = DB.engine)
    
if not inspect(DB.engine).has_table(ProductColor.ProductColor.__tablename__):
    ProductColor.ProductColor.__table__.create(bind = DB.engine)

if __name__ == '__main__':
    app.run(host= '0.0.0.0' , port='3000')

