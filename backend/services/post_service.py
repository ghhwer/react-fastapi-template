from sqlalchemy.orm import Session
from models.post import Post
from uuid import uuid4

class PostService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_posts(self):
        return self.db.query(Post).all()

    def get_post_by_id(self, post_id: str) -> Post:
        return self.db.query(Post).filter(Post.id == post_id).first()

    def create_new_post(self, title: str, content: str, user_id: str) -> Post:
        post = Post(id=str(uuid4()), title=title, content=content, user_id=user_id)
        self.db.add(post)
        return post