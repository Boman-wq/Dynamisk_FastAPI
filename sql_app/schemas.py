from pydantic import BaseModel, Field

#Scheme for all users 
class User(BaseModel):
    id: int
    email: str
    f_name: str
    l_name: str
    presentation: str = Field(max_length=512, default="")
    class Config:
        orm_mode = True

#Scheme for creating new users
class UserCreate(BaseModel):
    email: str
    f_name: str
    l_name: str

# Deleting a user by email
class UserDelete(BaseModel):
    email: str
    class Config:
        orm_mode = True