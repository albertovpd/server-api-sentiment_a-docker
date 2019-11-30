from bottle import route, run, get, post, request
import random
from bson.json_util import dumps
from populate import db,coll
import json
from bson.json_util import dumps



@get("/")
def index():
    return dumps(coll.find())
run(host="localhost", port=8080)


    

'''from bottle import route, run, get, post, request
import random
from mongo import CollConection
import bson

@get("/")
def index():
    return {
        "nombre": random.choice(["Pepe", "Juan", "Fran", "Luis"])
    }


@get("/chiste/<tipo>")
def demo2(tipo):
    print(f"un chiste de {tipo}")
    if tipo == "chiquito":
        return {
            "chiste": "Van dos soldados en una moto y no se cae ninguno porque van soldados"
        }
    elif tipo == "eugenio":
        return {
            "chiste": "Saben aquell que diu...."
        }
    else:
        return {
            "chiste": "No puedorrr!!"
        }

@post('/add')
def add():
    print(dict(request.forms))
    autor=request.forms.get("autor")
    chiste=request.forms.get("chiste")  
    return {
        "inserted_doc": str(coll.addChiste(autor,chiste))}


coll=CollConection('project2911','chats_sentiment_analysis')
run(host='0.0.0.0', port=8080)

'''