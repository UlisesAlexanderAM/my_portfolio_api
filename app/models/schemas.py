"""Module that stores the Pydantic models/schemas."""

from pydantic import BaseModel, Field


class SkillBase(BaseModel):
    """Base model/schema for skill."""

    name: str = Field(max_length=30)
    level: float = Field(ge=0, le=1)


class SkillCreate(SkillBase):
    """Model representing the data needed to create a skill in the DB (Is the same a SkillBase)."""

    pass


class Skill(SkillBase):
    """Model representing the skill in the DB"""

    id: int

    class Config:
        orm_mode = True
