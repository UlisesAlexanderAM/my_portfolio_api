"""Module to store the configuration and initialization of the SQLite DB."""
from pathlib import Path
import pydantic_settings
import sqlalchemy
from sqlalchemy import orm, pool


class DBSettings(pydantic_settings.BaseSettings):
    SQLITE_URL: str = "sqlite://"
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env"
    )


settings = DBSettings()

engine = sqlalchemy.create_engine(
    settings.SQLITE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
    poolclass=pool.StaticPool,
)

TestLocalSession = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
