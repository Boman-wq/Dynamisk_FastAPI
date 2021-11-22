from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# link to the database
SQLALCHEMY_DATABSE_URL = "sqlite:///./user.db" 

#create engine instance
engine = create_engine(
    SQLALCHEMY_DATABSE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()