import shelve
from wtforms import Form, SelectField

class PaymentForm(Form):
    payment_method = SelectField('Payment Method', choices=[('credit_card', 'Credit Card'), ('paypal', 'Paypal')])

def StockValidate(cart):
     db = shelve.open("products.db", flag='r')
     product = db["key"]
     stock = product['stock']
     for item in cart:
        if item['quantity'] > product['stock']:
            print("We do not have stock for that")

