"""Module to store the configuration and initialization of the SQLite DB."""
import pydantic
import sqlalchemy
from sqlalchemy import orm


class DBSettings(pydantic.BaseSettings):
    SQLITE_URL: str = "sqlite:///./database.db"

    class Config:
        env_file = ".env"


settings = DBSettings()

engine = sqlalchemy.create_engine(
    settings.SQLITE_URL, echo=True, connect_args={"check_same_thread": False}
)

LocalSession = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = orm.declarative_base()
