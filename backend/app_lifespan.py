from contextlib import asynccontextmanager
from fastapi import FastAPI
from application_logging import log_message
from repositories.database.database import get_db_session
from services.user_service import UserService

from services.post_service import PostService

def app_start_database_things():
    # Transaction 1
    with get_db_session() as db:
        log_message("DATA_STARTER", {"message": "post_db_init reached"})
        user_service = UserService(db)
        post_service = PostService(db)
        user = user_service.get_user_by_external_auth_id("root_id")
        if not user:
            log_message("DATA_STARTER", {"message": "root user not found, creating it"})
            user = user_service.create_new_user("Ghhwer", "", "root_id")
            post_service.create_new_post(title="Hello Template", content="I'm Ghhwer and this is an example post", user_id=user.id)
    

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This is on startup
    app_start_database_things()
    yield
    # This is on shutdown