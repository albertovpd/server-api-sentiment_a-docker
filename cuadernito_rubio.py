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



