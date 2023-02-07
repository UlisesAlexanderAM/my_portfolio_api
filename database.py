"""Module to handle the operations related to the SQLite DB."""

from sqlite3 import Connection, connect
from os import getenv
from typing import Dict

from dotenv import dotenv_values

config: Dict[str, str | None] = dotenv_values(".env")


def connect_db(fallback_db: str) -> Connection:
    """Function to connect to a SQLite database.

    Args:
        fallback_db (str): Name of a fallback database
                           if isn't declared in the enviroment.

    Returns:
        Connection: Object with the connectio to the database.
    """
    return connect(getenv("DB", fallback_db))


def close_connection_db(connection: Connection) -> None:
    """Function to close the connection to the database

    Args:
        connection (Connection): the object with the connection to the database
    """
    connection.close()
