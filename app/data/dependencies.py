"""Contains the dependencies for the FastAPI application."""

from app.database import database
from sqlalchemy import orm


def get_db():
    """Get an open database session.

    Yields:
        An open database session
    """
    db: orm.Session = database.LocalSession()
    try:
        yield db
    finally:
        db.close()

