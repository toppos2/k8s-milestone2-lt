from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:8088"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/name")
def get_name():
    return {"name": "Leander Tops"}

@app.get("/container-id")
def get_container_id():
    return {"container_id": socket.gethostname()}

@app.get("/health")
def health():
    return {"status": "ok"}
