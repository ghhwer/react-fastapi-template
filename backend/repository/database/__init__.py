from .database import engine
from .base import Base
from model.user import User  # noqa: F401  # Import to register the model
from model.post import Post  # noqa: F401  # Import to register the model

def init_models():
    """Initialize the database models."""
    Base.metadata.create_all(bind=engine)

# For async
#async def init_models():
#    """Initialize the database models."""
#    async with engine.begin() as conn:
#        await conn.run_sync(Base.metadata.create_all)