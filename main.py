from typing import Optional, List
from fastapi import FastAPI, HTTPException, Body, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import sys
from sql_app import database, crud, models, schemas
from http import HTTPStatus
import logging


models.Base.metadata.create_all(bind=database.engine)

## Main Program ##

app = FastAPI()

def main():
    app


def get_db():
    db=database.SessionLocal()
    try:
        yield db
    finally:
        db.close
# Schema

class Item(BaseModel):
    id: int
    email: str
    f_name: str
    l_name: str
    
    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "email": "",
                "f_name": "",
                "l_name": "",
            }
        }

# GET {user_id}, GET /users, PUT/users, POST /users, DELETE / users.

# Get Specific User by ID
@app.get("/users/{user_id}", response_model= schemas.User)
def read_user():
    return 0

# Get All Users
@app.get("/users/", response_model = List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# Update Specific User by ID
@app.put("/users/")
def update_user(
    item_id: int,
    item: Item = Body(
        ...,
        example={
            "id": 2,
            "email": "HelloPapiChulo@hotmail.com",
            "f_name": "Papi",
            "l_name": "Chulo",
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results

# Add User
@app.post("/users/", response_model = schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user
    # users = crud.create_user(db,email = user.email)
    # if users:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    # return users

# Delete Specific User by Email
@app.delete("/users/", response_model = schemas.UserDelete)
def delete_user(user: schemas.UserDelete, db: Session = Depends(get_db)):
    # db_user= crud.delete_user_by_email(db, user.email)
    # return db_user
    try:
        db_user = crud.delete_user_by_email(db, user.email)
        return db_user #HTTPStatus.OK.value
    except Exception as ex:
        print(ex)
    
if __name__ == "__main__":
    main()
    sys.exit(main())

#uvicorn main:app --reload
#ctrl k+c = comment / k+u = uncomment.