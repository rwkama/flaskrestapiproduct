"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request, jsonify, make_response
from DataProduct import DataProduct
import jsonpickle

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
@app.route('/')
def hello():
    return "Welcome to Rest Api Products Flask Python"

@app.route('/getProducts')
def listproducts():
   products=DataProduct.getProducts()
   jsonproducts = jsonpickle.encode(products,unpicklable=False)
   return jsonproducts
@app.route('/getProduct/<id>')
def searchproduct(id):
   product=DataProduct.getProduct(id)
   jsonproduct = jsonpickle.encode(product,unpicklable=False)
   return jsonproduct
    

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
