from pymongo import MongoClient
import string
from random import choices

mongo = MongoClient(port=27017)
print(mongo.list_database_names())
db = mongo['my_test_db']
users = db['users']
orders = db['orders']
goods = db['goods']

def create_user(name=None, cell=None, orders=[], disc=0):
    err = 'FORMAT MUST BE: name: str, cell: str, orders(Optional): list, disc(Optional): int'
    if None in [name, cell]:
        return err, False
    u = {'name': name, 'cell': cell, 'orders': orders, 'discount': disc}
    res = users.insert_one(u)
    print(f'New user was added to DB with result: {res}')
    return None, True

# stage => {'ordered', 'paid', 'delivered'}
# [{'good_id':['S', 'Red']}]

def create_order(stage=None, ord_price=0, goods=[]):
    err = 'FORMAT MUST BE: stage: {ordered, paid, delivered}, ord_price: int, goods: list '
    if stage is None:
        return err, False
    order_id = create_order_id()
    my_order = {'order_id': order_id , 'stage': None, 'order_price': 0.0, 'goods': []}
    res = users.insert_one(my_order)
    print(f'New order was added to DB with result: {res}')
    return None, True


def create_goods(size=[], descr=None, brand=None, color=[], price_tag=None):
    err = 'FORMAT MUST BE: size: list, descr: str, brand: str, color: list, price_tag: float '
    if price_tag is None or brand is None:
        return err, False
    good_id = create_slug()
    g = {'good_id': good_id, 'size': size, 'description': descr, 'brand': brand,
    'color': color, 'price_tag': price_tag}
    res = goods.insert_one(g)
    print(f'New good was added to DB with result: {res}')
    return None, True


def create_slug():
    return ''.join(choices(string.ascii_uppercase + string.digits, k=5))

def create_order_id():
    n_id = random.randint(1000000, 9999999)
    return n
    