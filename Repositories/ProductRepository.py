from asyncio.windows_events import NULL
from typing import List
from OrmModels.ProductColor import ProductColor
from OrmModels.ProductSize import ProductSize
from OrmModels.Products import Product
from sqlalchemy.orm import joinedload
from OrmModels.DB import session
import time

class ProductRepository:
    def __init__(self):
        self.db = session
        
    def getAll(self):
        products = self.db.query(
                Product
            ).filter(
                Product.delete_time == None
            ).options(
                joinedload(Product.category),
                joinedload(Product.sizes),
            ).all()
        products_data = [product.serialize() for product in products]
        return products_data

    def update(self,product_id:int , name:str , code_id:int , category_id:int , size_ids:list , unit_price:int, inventory:int ,color_ids:list):
        update_time = int(time.time()) 
        product = self.db.query(Product).get(product_id)
        product.name = name
        product.code_id = code_id
        product.category_id = category_id
        product.unit_price = unit_price
        product.inventory = inventory
        product.update_time = update_time
        self.db.merge(product)

        self.db.query(ProductSize).filter(ProductSize.product_id == product_id).delete()
        for id in size_ids:
            product_size = ProductSize(product_id=product.id, size_id=id)
            self.db.add(product_size)

        self.db.query(ProductColor).filter(ProductColor.product_id == product_id).delete()
        for id in color_ids:
            product_color = ProductColor(product_id=product.id ,color_id=id)
            self.db.add(product_color)

        self.db.commit()

    def create(self,name:str , code_id:int , category_id:int , size_ids:list , unit_price:int, inventory:int ,color_ids:list):
        
        product = Product(name , code_id, category_id, unit_price, inventory)
        self.db.add(product)
        self.db.flush()  
        for id in size_ids:
            product_size = ProductSize(product_id=product.id, size_id=id)
            self.db.add(product_size)
        for id in color_ids:
            product_color = ProductColor(product_id=product.id ,color_id=id)
            self.db.add(product_color)
        self.db.commit()
    
    def delete(self , product_id:int):
        delete_time = int(time.time()) 
        self.db.query(Product).filter(Product.id == product_id).update({Product.delete_time:delete_time})
        self.db.commit()