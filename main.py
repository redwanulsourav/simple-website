from bottle import route, run, template, request
from setup import Customer, Order
from peewee import * 
from datetime import *

db = SqliteDatabase("orders.db")

@route('/hello/<name>')
def hello(name='Stranger'):
    return template("Hello {{name}}, how are you?", name=name)


@route('/')
@route('/index')
def index():
    return template('index.tpl')

@route('/order')
def orders():
    orders = Order.select()
    return template('orders.tpl',orders=orders)

@route('/add_order')
def add_order():
    return template('add_order.tpl')

@route('/add_order',method='POST')
def add_order2():
    product_name = request.forms.get("product_name")
    product_price = request.forms.get("product_price")
    customer_name = request.forms.get("customer_name")

    customer = Customer.select().where(customer_name==customer_name)
    ordered_on = date(2021, 2, 11)

    order = Order(product_name = product_name, customer = customer, ordered_on = ordered_on, product_price = product_price)
    order.save()

    return template('index.tpl')

@route('/add_customer')
def add_customer():
    return template('add_customer.tpl')

@route('/add_customer',method="POST")
def add_customer2():
    customer_name = request.forms.get("customer_name")
    customer_address = request.forms.get("customer_address")
    customer_email = request.forms.get("customer_email")

    customer = Customer(customer_name = customer_name, customer_address = customer_address, customer_email = customer_email)
    customer.save()
    
    return template('index.tpl')

@route('/view_customer')
def view_customer():
    customers = Customer.select()
    return template('view_customer.tpl', customers=customers)
    

@route('/edit_customer/<customer_name>')
def edit_customer(customer_name):
    customer = Customer.select().where(customer_name==customer_name).get()
    return template('edit_customer.tpl', customer=customer)

@route('/edit_customer/<customer_name>', method="POST")
def edit_customer(customer_name):
    customer = Customer.select().where(customer_name==customer_name).get()
    customer.customer_address = request.forms.get('customer_address')
    customer.customer_email = request.forms.get('customer_email')
    customer.save()
    return template('index.tpl')

@route('/edit_order/<product_name>/<customer_name>/<product_price>')
def edit_order(product_name, customer_name, product_price):
    order = Order.select().where(product_name==product_name and product_price==product_price).get()
    return template('edit_order.tpl',order=order)

@route('/edit_order/<product_name>/<customer_name>/<product_price>', method='POST')
def edit_order2(product_name, customer_name, product_price):
    order = Order.select().where(product_name==product_name and product_price==product_price).get()
    order.product_name = request.forms.get('product_name')
    order.product_price = request.forms.get('product_price')
    order.save()
    return template('index.tpl')

@route('/delete_order/<product_name>/<customer_name>/<product_price>')
def delete_order(product_name, customer_name, product_price):
    order = Order.select().where(product_name==product_name and product_price==product_price).get()
    order.delete_instance()
    return template('index.tpl')

@route('/view_customer_details/<customer_name>')
def customer_details(customer_name):
    
    orders = Order.select().join(Customer).where(Customer.customer_name==customer_name)
    return template('customer_details.tpl',orders=orders)

run(host='localhost', port=8080, debug=True)