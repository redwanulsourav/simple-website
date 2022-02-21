from peewee import *

db = SqliteDatabase('orders.db')


class Customer(Model):
    customer_name = CharField()
    customer_address = CharField()
    customer_email = CharField()
    
    class Meta:
        database = db

class Order(Model):
    product_name = CharField()
    customer = ForeignKeyField(Customer, backref='orders')
    ordered_on = DateField()
    product_price = IntegerField()

    class Meta:
        database = db

db.connect()
db.create_tables([Customer, Order])