import os
import time
import random
import json
import paho.mqtt.client as mqtt

broker = os.getenv("MQTT_BROKER", "localhost")
port = int(os.getenv("MQTT_PORT", 1883))
topic = "devices/device123/telemetry"

client = mqtt.Client()
client.connect(broker, port, 60)

print(f"Connected to MQTT broker at {broker}:{port}")

while True:
    data = {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2),
        "device_id": "device123",
        "timestamp": time.time()
    }

    client.publish(topic, json.dumps(data))
    print(f"Published: {data}")
    time.sleep(5)
