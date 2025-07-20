from fastapi import FastAPI, Depends
from application_logging import log_message, log_exception

from views.post_view import PostView
from repositories.database.database import get_db
from services.post_service import PostService

route = FastAPI(title="posts-api")

@route.get("/")
def get_all_posts(db = Depends(get_db)) -> list[PostView]:
    post_service = PostService(db)
    all_posts = post_service.get_all_posts()
    # Convert to view
    post_views = [
        PostView(
            id=post.id,
            title=post.title,
            content=post.content
        )
        for post in all_posts
    ]
    return post_views