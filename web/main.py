from fastapi import FastAPI
from . import database, models, mqtt

app = FastAPI()

@app.on_event("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)
    mqtt.start_mqtt()

@app.get("/")
def read_root():
    return {"message": "IoT Web Receiver Online"}
