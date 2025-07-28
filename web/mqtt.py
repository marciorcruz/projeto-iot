import os
import json
import paho.mqtt.client as mqtt
from .database import SessionLocal
from .models import Telemetry

broker = os.getenv("MQTT_BROKER", "localhost")
port = int(os.getenv("MQTT_PORT", 1883))
topic = os.getenv("MQTT_TOPIC", "devices/device123/telemetry")

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code", rc)
    client.subscribe(topic)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        db = SessionLocal()

        telemetry = Telemetry(
            device_id=data.get("device_id"),
            temperature=data.get("temperature"),
            humidity=data.get("humidity"),
        )
        db.add(telemetry)
        db.commit()
        db.close()

        print("Data saved:", data)
    except Exception as e:
        print("Error saving data:", e)

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, 60)
    client.loop_start()
