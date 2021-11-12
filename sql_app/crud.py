from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate

def get_users(db:Session):
    return db.query(User).all()

def create_users(db: Session, user: UserCreate):
    db_user = User(email = user.email, f_name = user.f_name, l_name = user.l_name, presentation="No Presentation")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_by_email(db: Session, user_email: str):
    db_user = db.query(User).filter(User.email == user_email).first()
    db.delete(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return 0