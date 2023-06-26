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
        __name_pos="ID", __type_pos=sqlalchemy.Integer, primary_key=True
    )
    name: orm.Mapped[str] = orm.mapped_column(
        __name_pos="Name", __type_pos=sqlalchemy.String(length=30)
    )
    level: orm.Mapped[float] = orm.mapped_column(
        __name_pos="Level", __type_pos=sqlalchemy.Float
    )
