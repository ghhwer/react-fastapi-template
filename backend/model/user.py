from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from repository.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    surname = Column(String)
    external_auth_id = Column(String, unique=True)
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"