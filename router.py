from flask import Blueprint
from Controllers.ProductController import ProductController
from Middlewares.JWTMiddleware import JWTMiddleware
allRoute = Blueprint('allRoute', __name__)

@allRoute.get('/products')
def getProducts(): return ProductController().getAll()

@allRoute.post('/product')
def createProduct():return ProductController().create()

@allRoute.put('/product/<product_id>')
def updateProduct(product_id):return ProductController().update(product_id)

@allRoute.delete('/product/<product_id>')
def deleteProduct(product_id):return ProductController().delete(product_id)