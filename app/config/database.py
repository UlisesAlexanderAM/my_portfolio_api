"""Module to store the configuration and initialization of the SQLite DB."""
from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DBSettings(BaseSettings):
    SQLITE_URL: str = "sqlite:///./database.db"

    class Config:
        env_file = ".env"


settings = DBSettings()

engine = create_engine(settings.SQLITE_URL, connect_args={"check_same_thread": False})

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
