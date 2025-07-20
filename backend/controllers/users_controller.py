from fastapi import FastAPI, Depends
from application_logging import log_message, log_exception

from views.user_view import UserView
from repositories.database.database import get_db
from services.user_service import UserService

route = FastAPI(title="users-api")

@route.get("/")
def get_all_users(db = Depends(get_db)) -> list[UserView]:
    user_service = UserService(db)
    all_users = user_service.get_all_users()
    # Convert to view
    users_views = [
        UserView(
            id=user.id,
            name=user.name,
            surname=user.surname
        )
        for user in all_users
    ]
    return users_views