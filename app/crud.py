"""Module with the functions (CRUD) to interact with the database."""
from sqlalchemy import orm

from app.models import models, schemas


def get_skills(db: orm.Session) -> list[models.Skill]:
    """Retrieve all the skills from the database.

    Args:
        db: Manages the operation for the database

    Returns:
        List of skills
    """
    return db.query(models.Skill).all()


def save_skill(db: orm.Session, skill: schemas.SkillCreate) -> None:
    """Add/save a skill into the database.

    Args:
        db: Manages the operations for the database
        skill: Data describing a skill (name, level)
    """
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
