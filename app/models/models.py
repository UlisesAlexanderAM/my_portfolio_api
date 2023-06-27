"""SQLAlchemy models."""

import sqlalchemy
from sqlalchemy import orm

from app.config import database as db


class Skill(db.Base):
    """Skill table.

    - id (int): ID of the skill
    - name(str): Name of the skill
    - level(float): Level of the skill
    """

    __tablename__: str = "skill"

    id: orm.Mapped[int] = orm.mapped_column(
        __type_pos=sqlalchemy.Integer, primary_key=True
    )
    name: orm.Mapped[str] = orm.mapped_column(index=True)
    level: orm.Mapped[float]
