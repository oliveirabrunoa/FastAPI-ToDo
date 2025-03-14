from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine=create_engine('sqlite:///todo.db',connect_args={"check_same_thread": False})

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
