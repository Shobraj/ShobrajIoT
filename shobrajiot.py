from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_mqtt import Mqtt

#App init
app = Flask(__name__)

#Database init
app.config.from_pyfile('config.py')
#app.config.from_pyfile('myconfig.py')
db = SQLAlchemy(app)

#mqtt init
#mqtt = Mqtt(app)

from views import *

if __name__ == '__main__':
    db.create_all()
    app.run()