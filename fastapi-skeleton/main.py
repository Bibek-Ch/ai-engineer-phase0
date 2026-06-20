from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()



#data model for incoming item
class ItemRequest(BaseModel):
    name: str

#in-memory storage and the /item POST endpoint

#this list hold all the items temporarily
items_db = []

#create health check
@app.get("/health")
def health_check():
    return{"status":"ok"}

@app.post("/items")
def create_item(item: ItemRequest):
    new_item = {"id": str(uuid.uuid4()), "name": item.name}
    items_db.append(new_item)
    return new_item





