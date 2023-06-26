from app.config import database
from sqlalchemy import orm


def get_db():
    db: orm.Session = database.LocalSession()
    try:
        yield db
    finally:
        db.close()
