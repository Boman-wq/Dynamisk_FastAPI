# from sql_app import database, Base
from .database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    id=Column(Integer, primary_key=True, unique=True)
    email=Column(String)
    f_name=Column(String)
    l_name=Column(String)
    presentation=Column(String(512), default="")
