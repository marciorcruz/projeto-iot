import os
import time
import random
import json
import paho.mqtt.client as mqtt

broker = os.getenv("MQTT_BROKER", "localhost")
port = int(os.getenv("MQTT_PORT", 1883))
device_id = os.getenv("MQTT_DEVICE_ID", "device123")
topic = f"devices/{device_id}/telemetry"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(broker, port, 60)

# ✅ Importante: inicia o loop de rede
client.loop_start()

print(f"✅ Connected to MQTT broker at {broker}:{port}")

while True:
    data = {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2),
        "device_id": device_id,
        "timestamp": time.time()
    }

    result = client.publish(topic, json.dumps(data))
    status = result[0]

    if status == 0:
        print(f"📡 Published: {data}")
    else:
        print("❌ Failed to send message")

    time.sleep(20)
