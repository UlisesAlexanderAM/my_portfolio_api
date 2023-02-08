""" Module that defines the dataclass and functions related to skills. """

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from database import create_engine


class Skill(DeclarativeBase):
    """Class defining the skill table

    Args:
        DeclarativeBase (_type_): Class used for declarative class definition
    """

    __tablename__ = "skill"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    level: Mapped[float]


def create_skill_table() -> None:
    """Funtion that create the skill table"""
    engine = create_engine()
    Skill.metadata.create_all(engine)


def obtain_name_stin(message: str) -> str:
    """Function that ask for the name of the skill.

    Args:
        message (str): message show to the user

    Returns:
        str: name of the skill
    """
    return input(message)


def obtain_level_stin(message: str) -> str:
    """Function that ask for the level of the skill

    Args:
        message (str): message shown to the user

    Returns:
        str: skill level
    """
    return input(message)
