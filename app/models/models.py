"""Database models."""
from typing import Optional
import beanie
import pymongo


class Skills(beanie.Document):
    """Skills model."""

    name: str
    description: Optional[str] = None

    class Settings:
        indexes = pymongo.IndexModel("name", unique=True)


class Projects(beanie.Document):
    """Projects model."""

    name: str
    description: Optional[str] = None

    class Settings:
        indexes = pymongo.IndexModel("name", unique=True)
