import os
basrdir = os.path.abspath(os.path.dirname(__file__))

MQTT_BROKER_URL = "iot.eclipse.org"
MQTT_BROKER_PORT = 443
MQTT_USERNAME = 'shob'
MQTT_PASSWORD = 'qwer1234'
MQTT_KEEPALIVE = 1
MQTT_TLS_ENABLED =False


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI'   
    
    )