# hca.py
# Hardware Connector Application
import time
from mqtt_client_wrapper import MQTTClientWrapper

server="localhost"
clientId = f'raspberry-hca-sub-{time.time_ns()}'
username = "mqttuser"
password = "mqtt"
topicsToSubscribe = ["xpanse/sensordata/request"]
client = MQTTClientWrapper(server, clientId, username, password)

def main():
    client.setCallback(sub)
    client.connect()
    client.subscribeToTopics(topicsToSubscribe)
    while True:
        if True:
            client.waitForMessage()

def generate_sensor_data():
    # round(random.uniform(0.0,20.0), 2)
    sensor_data = {
        "timestamp": int(time.time()),
        "device_id":"dev123",
        "sensor_id":"sensor123",
        "data":{"windspeed": 5.9}
    }
    return sensor_data

def publishMessage(topic, msg):
    client.publishMessage(topic,msg)

def sub(topic, msg):
    print('-------------------------------------------------------------------')
    print('received message %s on topic %s' % (msg, topic))
    responseTopic = 'xpanse/sensordata/response'
    responseMsg = str(generate_sensor_data())
    publishMessage(responseTopic, responseMsg)

main()