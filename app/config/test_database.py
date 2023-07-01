"""Module to store the configuration and initialization of the SQLite DB."""
import pydantic
import sqlalchemy
from sqlalchemy import orm, pool
from sqlalchemy.ext import declarative


class DBSettings(pydantic.BaseSettings):
    SQLITE_URL: str = "sqlite://"

    class Config:
        env_file = ".env"


settings = DBSettings()

engine = sqlalchemy.create_engine(
    settings.SQLITE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
    poolclass=pool.StaticPool,
)

TestLocalSession = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
