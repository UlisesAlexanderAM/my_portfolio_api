"""Module with the functions (CRUD) to interact with the database."""
from sqlalchemy import orm

from app.models import models, schemas


def save_skill(db: orm.Session, skill: schemas.SkillCreate):
    """Add/save a skill into the database.

    Args:
        db (Session): Manages the operations for the database
        skill (schemas.SkillCreate): Data describing a skill (name, level)
    """
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
