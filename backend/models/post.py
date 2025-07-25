from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from repositories.database.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(String, ForeignKey("users.id"))

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title}, content={self.content})"