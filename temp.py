from Cart import *
import shelve

with shelve.open('shopping_cart.db', 'c') as db:
    obj = Cart("Milk", "20", "20", "9.99")
    db['1'] = obj
    obj2 = Cart("Clothes", "5", "5", "19.99")
    db['2'] = obj2
    obj3 = Cart("Eggs", "20", "20", "3.99")
    db['3'] = obj3
