from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from populate import db,coll
import json
from bson.json_util import dumps


@get("/")
def index():
    return dumps(coll.find())
#run(host="localhost", port=8080)


@get("/chat/<chat_id>/list")
def getChat(chat_id):    
    
    
    db, coll = connectCollection('chats','messages')    
    db, collchat = connectCollection('chats','chats')
    chatid_data = list(collchat.find({'Chat_id':int(chat_id)}))
    chat_obj_id = chatid_data[0].get('_id')
    chat_data = list(coll.find({'idChat':chat_obj_id}))
    ret = {}
    for i in range(len(chat_data)):
        name = chat_data[i].get('userName')
        message = chat_data[i].get('text')
        date = chat_data[i].get('datetime')
        ret[f'{name}_{date}'] = message         
    return ret

#---  running server  ---- 
run(host='0.0.0.0', port=8080)



