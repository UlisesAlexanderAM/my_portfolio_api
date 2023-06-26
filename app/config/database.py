"""Module to store the configuration and initialization of the SQLite DB."""
import pydantic
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.ext import declarative


class DBSettings(pydantic.BaseSettings):
    SQLITE_URL: str = "sqlite:///./database.db"

    class Config:
        env_file = ".env"


settings = DBSettings()

engine = sqlalchemy.create_engine(
    settings.SQLITE_URL, connect_args={"check_same_thread": False}
)

LocalSession = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()
