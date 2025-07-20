from pydantic import BaseModel

class PostView(BaseModel):
    id: str
    title: str
    content: str