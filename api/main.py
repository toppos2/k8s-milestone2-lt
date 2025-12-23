from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/name")
def get_name():
    return {"name": "Leander Tops"}

@app.get("/container-id")
def get_container_id():
    return {"container_id": socket.gethostname()}

@app.get("/health")
def health():
    return {"status": "ok"}
