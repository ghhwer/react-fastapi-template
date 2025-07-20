from contextlib import asynccontextmanager
from fastapi import FastAPI
from application_logging import log_message, log_exception
from repository.database.database import get_db_session
from model.user import User
from uuid import uuid4

def app_start_database_things():
    with get_db_session() as db:
        log_message("DATA_STARTER", {"message": "post_db_init reached"})
        user = db.query(User).where(User.external_auth_id=="root_id")
        count = user.count()
        if count == 0:
            log_message("DATA_STARTER", {"message": "root user not found, creating it"})
            user = User(id=str(uuid4()), name="Ghhwer", surname="", external_auth_id="root_id")
            db.add(user)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This is on startup
    app_start_database_things()
    yield
    # This is on shutdown