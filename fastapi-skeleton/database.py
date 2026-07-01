from sqlalchemy import create_engine, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import sessionmaker, declarative_base
import uuid


DATABASE_URL = "postgresql://postgres:W7g%40p7w000@localhost/mydb" #connection string

engine = create_engine(DATABASE_URL) # engine: core interface to the database
SessionLocal = sessionmaker(bind= engine, autocommit = False, autoflush=False) #a factory that create new database session
Base = declarative_base() #parent class for all database models

#item model: mapps to a table called "items"
class Item(Base):
    __tablename__ = "items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable= False)


#function to create all table(run once at startup)
def init_db():
    Base.metadata.create_all(bind=engine)