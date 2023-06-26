from config import database as db
from sqlalchemy import orm


def get_db():
    db: orm.Session = db.LocalSession()
    try:
        yield db
    finally:
        db.close()
