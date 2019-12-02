from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from populate import db,coll
import json
from bson.json_util import dumps
from pymongo_code import connectCollection

@get("/")
def index():
    return dumps(coll.find())

@get("/user")
def getUsers():
    all_users=dumps(coll.find().distinct("userName"))
    return all_users

@get("/messages/")
def getChat():
    # get all the messages of all users
    return dumps(coll.find({},{"text":1,'_id':0}))

@get("/chatid/")
def getConversations():
    # get all the messages of all conversations
    return dumps(coll.find({},{'idChat':1,'text':1,'_id':0}))



@post('/user/create')
def createuser():
    '''
     create an user. it assinges automatically an ID
    '''
    name = str(request.forms.get("name"))
    new_id = coll.distinct("idUser")[-1] + 1
    new_user = {
        "idUser":new_id,
        "userName":name
    }
    
    coll.insert_one(new_user)

@post('/create_all')
def createall():
    '''
     create all fields of user. it assinges automatically an ID
    '''
    name = str(request.forms.get("name"))
    text = str(request.forms.get("text"))
    new_id = coll.distinct("idUser")[-1] + 1
    new_idm = coll.distinct("idMessage")[-1] + 1
    new_idc= coll.distinct("idChat")[-1] + 1
    new_user = {
        "idUser":new_id,
        "userName":name,
        "idMessage":new_idm,
        "idChat":new_idc,
        'text': text
    }    
    coll.insert_one(new_user)


#=============================================
#  cosas que no he usado todavía 
@post('chat/<chat_id>/addmessage')
def createMessage(chat_id):
    message = str(request.forms.get("message"))
    new_id = coll.distinct("idMessage")[-1] + 1
    new_message = {
        "idChat": chat_id,
        "idMessage":new_id,
        "text" : message
    }
    coll.insert_one(new_message)



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

@post('chat/<chat_id>/addmessage')
def createMessage(chat_id):
    message = str(request.forms.get("message"))
    new_id = coll.distinct("idMessage")[-1] + 1
    new_message = {
        "idChat": chat_id,
        "idMessage":new_id,
        "text" : message
    }
    coll.insert_one(new_message)


#---  running server  ---- 

# si usas el comando de debajo vas a tener errores a la hora de poner decoradores
#db, coll = connectCollection('project2911','chats_sentiment_analysis')
run(host='0.0.0.0', port=8080)

