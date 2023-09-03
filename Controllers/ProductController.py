from flask import request,make_response,jsonify,g
from Services.ProductService import ProductService 

class ProductController:
    def __init__(self):
        self.ProductService = ProductService()

    def getAll(self):
        try:
            print(g.token)
            result = self.ProductService.getAll()
            return make_response(
                    jsonify(
                        {"success":"true",
                        "result":result}
                    ),200)
        except Exception as msg:
            return make_response(
                jsonify(
                    {"success":"false","message":str(msg)}
                ),400)

    def create(self):
        try:
            if request.is_json:
                params = request.get_json()
                name = params.get('name', None)
                code_id = params.get('code_id', None)
                category_id = params.get('category_id', None)
                size_ids = params.get('size_ids', None)
                unit_price = params.get('unit_price', None)
                inventory = params.get('inventory', None)
                color_ids = params.get('color_ids', None)
            else:
                raise ValueError('data type error')
            self.ProductService.create(name , code_id , category_id , size_ids , unit_price , inventory , color_ids)
            return make_response(
                jsonify(
                    {"success":"true"}
                ), 200)

        except Exception as msg:
            return make_response(
                jsonify(
                    {"success":"false","message":str(msg)}
                ),400)

    def update(self,product_id):
        try:
            if request.is_json:
                params = request.get_json()
                name = params.get('name', None)
                code_id = params.get('code_id', None)
                category_id = params.get('category_id', None)
                size_ids = params.get('size_ids', None)
                unit_price = params.get('unit_price', None)
                inventory = params.get('inventory', None)
                color_ids = params.get('color_ids', None)
            else:
                raise ValueError('data type error')
                
            self.ProductService.update(product_id,name , code_id , category_id , size_ids , unit_price , inventory , color_ids)
            return make_response(
                jsonify(
                    {"success":"true"}
                ), 200)

        except Exception as msg:
            return make_response(
                jsonify(
                    {"success":"false","message":str(msg)}
                ),400)
    
    def delete(self , product_id:int):
        try:
            self.ProductService.delete(product_id)
            return make_response(
                jsonify(
                    {"success":"true"}
                ), 200)
        except Exception as msg:
            return make_response(
                jsonify(
                    {"success":"false","message":str(msg)}
                ),
                400)
