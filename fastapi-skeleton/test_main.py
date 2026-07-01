from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Item
import main


#use sqlite for testing
SQLITE_URL = "sqlite:///./test.db"
engine = create_engine(SQLITE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)

#create the tables in the DB
Base.metadata.create_all(bind=engine)

#override the get_db dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

main.app.dependency_overrides[main.get_db] = override_get_db

client = TestClient(main.app)

def test_create_and_get_items():
    #create item
    resp = client.post("/items", json={"name": "bread"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "bread"
    assert "id" in data

    #get all item
    resp = client.get("/items")
    assert resp.status_code == 200
    items =  resp.json()["items"]
    assert len(items)==1
    assert items[0]["name"]== "bread"

