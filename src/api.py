from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from populate import db,coll
import json
from bson.json_util import dumps
from pymongo_code import connectCollection
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
from functions import getSentimentReport, getFinalMetric

@get("/")
def index():
    '''
    returns everything in server
    '''
    return dumps(coll.find())

@get("/user")
def getUsers():
    '''
    find all users. There is another better function below
    '''
    all_users=dumps(coll.find().distinct("userName"))
    return all_users

@get("/messages/")
def getChat():
    '''
    get all the messages of all users
    '''
    return dumps(coll.find({},{"text":1,'_id':0}))

@get("/chatid/")
def getConversations():
    '''
    get all the messages of all conversations
    '''
    return dumps(coll.find({},{'idChat':1,'text':1,'_id':0}))

#-----------
# sentiment analysis
@get("/chat/<idChat>/sentiment/") 
def sentimentReport(idChat):
    """
    ---- Celia's function --- :D
    Returns a report with the sentiment metric from a chat_id
    """
    chat=dumps(coll.find({'idChat' :int(idChat)},{'userName':1,'text':1,'_id':0}))
    report=getSentimentReport(chat)
    return report
#-----------


# recommending system
@get("/users")
def getAllUsers():
    """Returns all users"""
    return dumps(coll.find({},{'userName':1,"text":1,'_id':0}))  


# @get("/chat/<idChat>/sentiment/")
# def getConversations(idChat):
#     # get the sentiment analysis of a given id chat
#     dumps(coll.find({"idChat":int(idChat)},{'idChat':1,'text':1,'_id':0}))
#     url='http://localhost:8080/idChat/'
#     chatid=requests.get(url).json()
#     chatid
#     my_dict = {}
#     for x in chatid:    
#         if 'idChat' in x:
#             if x['idChat'] not in my_dict:
#                 my_dict[x['idChat']] = x['text']
#             else:
#                 my_dict[x['idChat']] += " {}".format(x['text'])
#     list_conversation=my_dict[idChat]
#     sid = SentimentIntensityAnalyzer()
#     polarity=sid.polarity_scores(list_conversation)
#     return print("The chosen conversation with the chatId {} has the following clasification: \n".format(idChat),
#     polarity)

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
#  Testing decorators i did not use yet

# @post('chat/<chat_id>/addmessage')
# def createMessage(chat_id):
#     message = str(request.forms.get("message"))
#     new_id = coll.distinct("idMessage")[-1] + 1
#     new_message = {
#         "idChat": chat_id,
#         "idMessage":new_id,
#         "text" : message
#     }
#     coll.insert_one(new_message)



# @get("/chat/<chat_id>/list")
# def getChat(chat_id):    
#     db, coll = connectCollection('chats','messages')    
#     db, collchat = connectCollection('chats','chats')
#     chatid_data = list(collchat.find({'Chat_id':int(chat_id)}))
#     chat_obj_id = chatid_data[0].get('_id')
#     chat_data = list(coll.find({'idChat':chat_obj_id}))
#     ret = {}
#     for i in range(len(chat_data)):
#         name = chat_data[i].get('userName')
#         message = chat_data[i].get('text')
#         date = chat_data[i].get('datetime')
#         ret[f'{name}_{date}'] = message         
#     return ret

# @post('chat/<chat_id>/addmessage')
# def createMessage(chat_id):
#     message = str(request.forms.get("message"))
#     new_id = coll.distinct("idMessage")[-1] + 1
#     new_message = {
#         "idChat": chat_id,
#         "idMessage":new_id,
#         "text" : message
#     }
#     coll.insert_one(new_message)


#---  running server  ---- 

# si usas el comando de debajo vas a tener errores a la hora de poner decoradores
#db, coll = connectCollection('project2911','chats_sentiment_analysis')
run(host='0.0.0.0', port=8080)

