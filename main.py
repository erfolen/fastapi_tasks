from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/home")
def home():
    return {"Hi"}
