import pymongo
from pymongo import MongoClient

mongoClient = MongoClient('127.0.0.1', port = 27017)

print(mongoClient.list_database_names())

