from typing import Optional

from django import db

from fastapi import FastAPI
from pydantic import  BaseModel

app = FastAPI()
db=[]
class Wallet_System(BaseModel):
    wallet_owner: str
    money_wallet:int


@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get('/wallet')
def get_wallet():
    return db
@app.post('/wallet')
def create_wallet(wallet:Wallet_System):
    db.append(wallet.dict())
    return db[-1]