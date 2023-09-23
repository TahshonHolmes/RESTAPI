from flask import Flask, jsonify, request

app = Flask(__name__)


carts = {}

@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = carts.get(user_id, {})
    return jsonify(cart)

@app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id):
    quantity = request.get_json().get('quantity', 1)
    cart = carts.get(user_id, {})
    cart[product_id] = cart.get(product_id, 0) + quantity
    carts[user_id] = cart
    return jsonify({"message": "Product added to cart successfully"}), 200

@app.route('/cart/<int:user_id>/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(user_id, product_id):
    quantity = request.get_json().get('quantity', 1)
    cart = carts.get(user_id, {})
    if product_id in cart:
        cart[product_id] = max(cart[product_id] - quantity, 0)
        if cart[product_id] == 0:
            del cart[product_id]
    carts[user_id] = cart
    return jsonify({"message": "Product removed from cart successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
