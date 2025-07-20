from contextlib import asynccontextmanager
from fastapi import FastAPI
from application_logging import log_message
from repositories.database.database import get_db_session
from services.user_service import UserService

def app_start_database_things():
    with get_db_session() as db:
        log_message("DATA_STARTER", {"message": "post_db_init reached"})
        user_service = UserService(db)
        user = user_service.get_user_by_external_auth_id("root_id")
        if not user:
            log_message("DATA_STARTER", {"message": "root user not found, creating it"})
            user_service.create_new_user("Ghhwer", "", "root_id")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This is on startup
    app_start_database_things()
    yield
    # This is on shutdown