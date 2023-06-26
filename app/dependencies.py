from config.database import LocalSession
from sqlalchemy.orm import Session


def get_db():
    db: Session = LocalSession()
    try:
        yield db
    finally:
        db.close()
