#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json
import os

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = "mongodb+srv://vargas:{}@vargas-api-dtexi.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
def connectCollection(database, collection):    
client = MongoClient(connection)
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('project2911','chats_sentiment_analysis')

with open('chats.json') as f:
    chats_json = json.load(f)
coll.insert_many(chats_json)