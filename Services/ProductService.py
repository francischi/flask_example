from typing import List
from Repositories.ProductRepository import ProductRepository

class ProductService:
    def __init__(self):
        self.ProductRepository = ProductRepository()
        
    def getAll(self):
        return self.ProductRepository.getAll()

    def create(self, name:str , code_id:int, category_id:int, size_ids:List, unit_price:int , inventory:int , color_ids:List):
        if name is None or name=="":
            raise ValueError('name required')

        if code_id is None:
            raise ValueError('code required')

        if category_id is None:
            raise ValueError('category_id required')

        if unit_price is None or unit_price<0:
            raise ValueError('unit_price required')
        
        self.ProductRepository.create(name , code_id, category_id,size_ids, unit_price, inventory ,color_ids)

    def update(self, product_id:int ,  name:str , code_id:int, category_id:int, size_ids:List, unit_price:int , inventory:int , color_ids:List):
        if product_id is None or product_id=="":
            raise ValueError('product_id required')

        if name is None or name=="":
            raise ValueError('name required')

        if code_id is None:
            raise ValueError('code required')

        if category_id is None:
            raise ValueError('category_id required')

        if unit_price is None or unit_price<0:
            raise ValueError('unit_price required')
        self.ProductRepository.update(product_id,name , code_id, category_id,size_ids, unit_price, inventory ,color_ids)

    def delete(self , product_id:int):
        if product_id is None:
            raise ValueError('product_id required')
        return self.ProductRepository.delete(product_id)