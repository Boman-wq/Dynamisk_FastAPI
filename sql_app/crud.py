from sqlalchemy.orm import Session
from . import models
from .schemas import UserCreate, User

def get_users(db:Session):
    return db.query(models.User).all()

def create_user(db: Session, user: UserCreate):
    db_user = models.User(email = user.email, f_name = user.f_name, l_name = user.l_name, presentation="No Presentation")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_by_email(db: Session, user_email: str):
    db_user = db.query(models.User).filter(models.User.email == user_email).first()
    db.delete(db_user)
    db.commit()
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
    #db_user = db.query().get(user_id)

def update_user(db: Session, user: User):
    db_user = db.query(models.User).get(user.id)
    db_user.email = user.email
    db_user.f_name = user.f_name
    db_user.l_name = user.l_name
    db_user.presentation = user.presentation
    db.commit()
    return db_user