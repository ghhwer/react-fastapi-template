from sqlalchemy.orm import Session
from models.user import User
from uuid import uuid4

class UserService:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all_users(self,):
        return self.db.query(User).all()

    def get_user_by_external_auth_id(self, external_auth_id: str) -> User:
        """Get a user by email."""
        return self.db.query(User).filter(User.external_auth_id == external_auth_id).first()
    
    def create_new_user(self, name:str, surname:str, external_auth_id:str) -> User:
        user = User(id=str(uuid4()), name=name, surname=surname, external_auth_id=external_auth_id)
        self.db.add(user)
        self.db.flush()
        return user