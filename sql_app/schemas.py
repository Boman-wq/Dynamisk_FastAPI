from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    email: str
    f_name: str
    l_name: str
    presentation: str = Field(max_length=512, default="")
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str
    f_name: str
    l_name: str

class UserDelete(BaseModel):
    email: str