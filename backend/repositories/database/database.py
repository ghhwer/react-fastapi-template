from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

# Database connection URL
SQLALCHEMY_DATABASE_URL = "duckdb:///./database.db"

# Create a synchronous engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session maker
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Get a database session."""
    db = session()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

@contextmanager
def get_db_session():
    """Get a new database session."""
    db = session()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


# Foe Async...
#from sqlalchemy import create_engine
#from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
#from sqlalchemy.orm import sessionmaker
#from .base import Base
#
## Database connection URL
#SQLALCHEMY_DATABASE_URL = "duckdb:///./database.db"
#
## Create an async engine
#engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
#
## Create a session maker
#async_session = sessionmaker(
#    engine, class_ = AsyncSession, expire_on_commit=False
#)
#
#async def get_db():
#    """Get a database session."""
#    async with async_session() as session:
#        try:
#            yield session
#        finally:
#            await session.close()