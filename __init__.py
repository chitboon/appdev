from flask import Flask, render_template, request, redirect, url_for
from cartFunctions import StockValidate, PaymentForm
import shelve
from Cart import *

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    # this creates 5 dummy product
    init_products()
    # this is to clear cart
    clear_cart()
    product_list = get_products()
    return render_template('home.html', products = product_list)

@app.route('/add_cart/<string:id>')
def add_cart(id):
    cart = get_cart('xxx')
    print(cart.get_count())
    product = get_product(id)
    cart.add_item(product)
    save_cart(cart)
    cart = get_cart('xxx')
    print(cart.get_count())
    return render_template('displayCart.html', count=cart.get_count(), cart=cart)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_key = request.form.get("product_key")
    # db = shelve.open("products.db", flag='r')
    product = get_product(product_key)
    #if product_key in db:
        # product = db[product_key]\
    id = "123"
    cart = get_cart(id)
    cart = cart_db['Cart']
    if product['key'] in cart:
        cart[product['key']]['quantity'] += 1
    else:
        cart[product['key']] = {'name': product['name'], 'category': product['category'], 'price': product['price'], 'quantity': 1}
        cart_db['Cart'] = cart
        cart_db.close()
        db.close()
        return "Product added to cart successfully"

@app.route('/displayCart', methods=['GET', 'POST'])
def display_cart():
    cart_db = shelve.open('shopping_cart.db', 'c')
    print(cart_db)
    cart_list = []
    for key in cart_db:
        item = cart_db.get(key)
        cart_list.append(item)
    cart_db.close()
    return render_template('displayCart.html', count=len(cart_list), cart_list=cart_list)
    
@app.route('/addQuantity/<string:id>', methods=['POST', 'GET'])
def add_quantity(id):
    product_key = str(id)
    cart_db = shelve.open("shopping_cart.db", flag='c')
    cart = cart_db['Cart'] if 'Cart' in cart_db else {}
    if product_key in cart:
        cart[product_key][int('quantity')] += 1
        cart_db['Cart'] = cart
        cart_db.close()
        return "Cart updated successfully"
    else:
        cart_db.close()
        return "Error: Invalid product key"

@app.route('/subtractQuantity/<string:id>', methods=['POST', 'GET'])
def subtract_quantity(id):
    product_key = str(id)
    cart_db = shelve.open("shopping_cart.db", flag='c')
    cart = cart_db['Cart'] if 'Cart' in cart_db else {}
    if product_key in cart:
        cart[product_key][int('quantity')] -= 1
        cart_db['Cart'] = cart
        cart_db.close()
        return "Cart updated successfully"
    else:
        cart_db.close()
        return "Error: Invalid product key"

@app.route('/delete_cart/<string:id>', methods = ["POST", "GET"])
def remove_from_cart(id):
    product_key = str(id)
    print(product_key)
    cart_db = shelve.open("shopping_cart.db", flag='c')
    if product_key in cart_db.keys():
        print(cart_db.keys())
        del cart_db[product_key]
        cart_db.close()
        return redirect(url_for("display_cart"))
    else:
        cart_db.close()
        return "Error: Invalid product key"

@app.route('/invoice', methods=['GET', 'POST'])
def invoice():
    form = PaymentForm()
    cart_db = shelve.open('shopping_cart.db', 'r')
    cart = cart_db['Cart'] if 'Cart' in cart_db else {}
    cart_db.close()
    total_cost = sum(item['price'] * item['quantity'] for item in cart.values())
    if form.validate_on_submit():
        cart_db = shelve.open('shopping_cart.db', 'w')
        cart_db['Cart'] = {}
        cart_db.close()
        return redirect(url_for('success'))
    return render_template('invoice.html', form=form, cart=cart, total_cost=total_cost)

if __name__ == '__main__':
    app.run()
