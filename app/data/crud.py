"""Module with the functions (CRUD) to interact with the database."""

from collections import abc

import sqlalchemy
from sqlalchemy import orm

from app.models import models, schemas


def get_skills(db: orm.Session) -> abc.Sequence[models.Skill]:
    """Retrieve all the skills from the database.

    Args:
        db: Manages the operations of the database

    Returns:
        List of skills
    """
    statement = sqlalchemy.select(models.Skill)
    return db.scalars(statement=statement).fetchall()


def get_skill_by_name(db: orm.Session, skill_name: str) -> models.Skill | None:
    """Retrieve a skill given the name of the skill.

    Args:
        db: Manages the operation of the database
        skill_name: Name of the skill

    Returns:
        The skill with name == skill_name o None/null
    """
    statement = sqlalchemy.select(models.Skill).where(models.Skill.name == skill_name)
    return db.scalars(statement=statement).one_or_none()


def save_skill(db: orm.Session, skill: schemas.SkillCreate) -> None:
    """Add/save a skill into the database.

    Args:
        db: Manages the operations of the database
        skill: Data describing a skill (name, level)
    """
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
