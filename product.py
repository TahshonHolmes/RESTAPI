from flask import Flask, jsonify, request
import os
app = Flask(__name__)

products = [
    {"id": 1, "name": "Product A", "price": 10.0, "quantity": 100},
    {"id": 2, "name": "Product B", "price": 5.0, "quantity": 50},
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is not None:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price"),
        "quantity": data.get("quantity"),
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
