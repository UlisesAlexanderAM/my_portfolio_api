"""Module that stores the SQLAlchemy models."""

from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import Base


class Skill(Base):
    """Class/model defining the skill table."""

    __tablename__: str = "skill"
    id: Mapped[int] = mapped_column(
        __name_pos="ID", __type_pos=Integer, primary_key=True
    )
    name: Mapped[str] = mapped_column(__name_pos="Name", __type_pos=String(length=30))
    level: Mapped[float] = mapped_column(__name_pos="Level", __type_pos=Float)
