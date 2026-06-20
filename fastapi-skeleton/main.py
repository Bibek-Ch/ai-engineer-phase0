from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

#this list hold all the items temporarily
item_db = []

#pydentic model that describe JASON file

class ItemRequest(BaseModel):
    name : str


@app.get("/health")
def health_check():
    return{"status":"ok"}

@app.get("/items")
def get_items():
    return{"items": item_db}





@app.post("/items")
def create_list(item: ItemRequest):
    new_item = {"ID": str(uuid.uuid4()), "name": item.name}
    item_db.append(new_item)
    return new_item






