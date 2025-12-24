from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket
from pymongo import MongoClient
import os

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

MONGO_URL = "mongodb://mongo:27017"

client = MongoClient(MONGO_URL)
db = client["webstack"]
settings = db["settings"]


@app.get("/name")
def get_name():
    doc = settings.find_one({"_id": "profile"})
    if not doc:
        return {"name": "Unknown"}
    return {"name": doc["name"]}

@app.get("/container-id")
def get_container_id():
    return {"container_id": socket.gethostname()}

@app.get("/health")
def health():
    return {"status": "ok"}
