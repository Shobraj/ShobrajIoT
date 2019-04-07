
import paho.mqtt.subscribe as subscribe
import json
from shobrajiot import db
from models import Messages
from sqlalchemy import exc

def print_msg(client, userdata, message):
    payload = (message.payload).decode("utf-8").replace("'",'"')
    payloaddict = json.loads(payload)
    message = Messages(payloaddict['title'], payloaddict['body'])
    print("The data with title: '"+message.title+"' and body: '"+message.body+"' is received.")
    db.session.add(message)
    try:
        db.session.commit()
        print("message with title: '"+message.title+"' and body: '"+message.body+"' is store to Database")
    except exc.IntegrityError as e:
        db.session().rollback()
        print(e)
    except exc.SQLAlchemyError:
        pass
    

topic = 'shobrajmessage'
subscribe.callback(print_msg, topic, hostname="iot.eclipse.org")
