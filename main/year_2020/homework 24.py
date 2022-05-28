import faker
from datetime import datetime 
from pymongo import MongoClient
from datetime import datetime
fake = faker.Faker('en_US')


name = fake.name()
address = fake.address()
birthday = fake.date()
phone = fake.phone_number()
email = fake.email()


mongo = MongoClient('localhost', port=27017)
my_test_db = mongo['my_DB']
mongo_client = my_test_db['User_db']

user_to_insert = {'name':name,
                  'address':address,
                  'birthday':birthday,
                  'phone':phone,
                  'email':email,
                  'date': datetime.now()}
res = mongo_client.insert_one(user_to_insert)
