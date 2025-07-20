from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from repository.database.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(String, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title}, content={self.content})"