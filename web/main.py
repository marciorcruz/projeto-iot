from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database, models, mqtt

app = FastAPI(title="IoT Data Receiver", description="API para receber e visualizar dados IoT")

@app.on_event("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)
    mqtt.start_mqtt()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "IoT Web Receiver Online", "status": "running"}

@app.get("/telemetry")
def get_telemetry(limit: int = 10, db: Session = Depends(get_db)):
    """Retorna os últimos dados de telemetria"""
    telemetry_data = db.query(models.Telemetry).order_by(models.Telemetry.timestamp.desc()).limit(limit).all()
    return {
        "count": len(telemetry_data),
        "data": [
            {
                "id": t.id,
                "device_id": t.device_id,
                "temperature": t.temperature,
                "humidity": t.humidity,
                "timestamp": t.timestamp.isoformat() if t.timestamp else None
            }
            for t in telemetry_data
        ]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "iot-web-receiver"}
