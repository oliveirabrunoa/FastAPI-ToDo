from database import Base, engine
from models import Task 

print("Creating database tables...")

Base.metadata.create_all(bind=engine)
# This script creates the database tables based on the models defined in models.py.     
