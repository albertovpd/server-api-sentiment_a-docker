#!/home/vargas/miniconda3/envs/ironhack/bin/python

#from flask import *

from pymongo import MongoClient
import getpass
import json

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = 'mongodb+srv://admin_1019:{}@datamad1019-enj5c.mongodb.net/test?retryWrites=true&w=majority'.format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('project2911','chats_sentiment_analysis ')

query = {'_id':0}
test_query = coll.find(query)
print(list(test_query))