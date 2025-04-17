
from flask import Flask, request
from models import *

app = Flask(__name__)

# GET all products
@app.route('/products', methods=['GET'])
def get_all_products():
    return get_products()

# GET product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return get_product_by_id(product_id)

# POST a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    return add_product(data)

# POST multiple products
@app.route('/products/bulk', methods=['POST'])
def bulk_add_products():
    data = request.json
    return bulk_add(data)

# PUT to update full product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.json
    return update_product(product_id, data)

# PUT to update stock only
@app.route('/products/<int:product_id>/stock', methods=['PUT'])
def update_stock_route(product_id):
    stock = request.json.get('stock')
    return update_stock(product_id, stock)

# DELETE one product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    return delete_product(product_id)

# DELETE all products
@app.route('/products/all', methods=['DELETE'])
def delete_all_products_route():
    return delete_all_products()

if __name__ == '__main__':
    app.run(debug=True)
