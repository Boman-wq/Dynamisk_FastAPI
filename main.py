from typing import List
from fastapi import FastAPI,  Depends
from sqlalchemy.orm import Session
from sql_app import database, crud, models, schemas
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#access to database, read and disconnect when done#
def get_db():
    db=database.SessionLocal()
    try:
        yield db
    finally:
        db.close

# Get Specific User by ID#
@app.get("/users/{user_id}", response_model = schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    return db_user


# Get All Users and return to users list 
@app.get("/users/", response_model = List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# Update Specific User by ID
@app.put("/users/", response_model = schemas.User)
def update_user(user: schemas.User, db:Session = Depends(get_db)):
    db_user = crud.update_user(db, user)
    return db_user

# Add User and return user
@app.post("/users/", response_model = schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user

# Delete Specific User by Email
@app.delete("/users/", response_model = schemas.UserDelete)
def delete_user(user: schemas.UserDelete, db: Session = Depends(get_db)):
    db_user= crud.delete_user_by_email(db, user.email)
    return db_user

#To start run:
#uvicorn main:app --reload