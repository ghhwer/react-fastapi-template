from pydantic import BaseModel

class UserView(BaseModel):
    id: str
    name: str
    surname: str | None = None