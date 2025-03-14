from database import Base
from sqlalchemy import Column, Integer, String, Boolean
#from pydantic import BaseModel

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(400), nullable=True) 
    status = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task: {self.title}>"