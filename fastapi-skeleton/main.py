from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import SessionLocal, Item, init_db
from sqlalchemy.orm import Session


app = FastAPI()

#create table on startup
init_db()

#pydentic model that describe JASON file

class ItemRequest(BaseModel):
    name : str

#dependency: get database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/health")
def health_check():
    return{"status":"ok"}


@app.post("/items")
def create_list(item: ItemRequest, db: Session = Depends(get_db)):
    new_item = Item(name = item.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item) #get the generated id
    return {"id": str(new_item.id), "name": new_item.name}

@app.get("/items")
def get_items(db: Session= Depends(get_db)):
    items = db.query(Item).all()
    return {"items": [{"id": str(i.id), "name": i.name} for i in items]}






