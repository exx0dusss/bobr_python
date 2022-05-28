from pymongo import MongoClient
from datetime import datetime

mongo = MongoClient('localhost', port=27017)
all_db = mongo.list_database_names()
print(f'All Databases in Mongo: {all_db}')
my_test_db = mongo['my_test_db']
mongo_client = my_test_db['SSS']
user_to_insert = {'name':'TT'}
res = mongo_client.insert_one(user_to_insert)
print(res)
print(mongo.list_database_names())

database_list = mongo_client.database_names()
print ("database_list:", database_list)
print ("number of db:", len(database_list))