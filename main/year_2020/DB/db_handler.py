from pymongo import MongoClient
import string
from random import choices, randint

mongo = MongoClient('mongodb+srv://warehouse:warehouse00@cluster0.rwamk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
print(f'Connected to MongoAtlas: {mongo.list_database_names()}')
db = mongo['my_test_db']
users = db['users']
orders = db['orders']
goods = db['goods']


def create_user(name=None, cell=None, user_orders=[], disc=0):
    err = 'FORMAT MUST BE: name: str, cell: str, orders(Optional): list, disc(Optional): int'
    if None in [name, cell]:
        return err, False
    u = {'name': name, 'cell': cell, 'orders': user_orders, 'discount': disc}
    res = users.insert_one(u)
    print(f'New user was added to DB with result: {res}')
    return None, True


def create_order(stage=None, price=0.0, user_goods=[]):
    err = 'FORMAT MUST BE: stage: [ordered, paid, delivered], price: positive float, ' \
          'user_goods: list of goods'
    if stage is None or price == 0.0 or not user_goods:
        return err, False
    order_id = generate_id(7)
    my_order = {'order_id': order_id, 'stage': stage, 'order_price': price, 'goods': user_goods}


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


def generate_id(k):
    return ''.join([str(randint(1, 9)) for _ in range(k)])
