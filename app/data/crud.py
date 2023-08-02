"""Module with the functions (CRUD) to interact with the database."""

from collections import abc

from app.models import models


def get_skills(db):
    """Retrieve all the skills from the database.

    Args:
        db: Manages the operations of the database

    Returns:
        List of skills
    """
    pass


def get_skill_by_name(db, skill_name: str):
    """Retrieve a skill given the name of the skill.

    Args:
        db: Manages the operation of the database
        skill_name: Name of the skill

    Returns:
        The skill with name == skill_name o None/null
    """
    pass


