"""Module to handle the operations related to the SQLite DB."""

from typing import Dict
from sqlalchemy import engine_from_config, Engine

from dotenv import dotenv_values

config: Dict[str, str | None] = dotenv_values(".env")


def create_engine() -> Engine:
    """Function that create the engine object

    Returns:
        Engine: Engine object
    """
    return engine_from_config(config, "SQLALCHEMY_")
