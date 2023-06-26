"""Pydantic schemas/models.

The models are used for FastAPI to perform validations,
and generate documentation.
"""

import pydantic


class SkillBase(pydantic.BaseModel):
    """Base model/schema for skill."""

    name: str = pydantic.Field(max_length=30)
    level: float = pydantic.Field(ge=0, le=1)


class SkillCreate(SkillBase):
    """Model representing the data needed to create a skill in the DB (Is the same a SkillBase)."""

    pass


class Skill(SkillBase):
    """Model representing the skill in the database.

    This models adds the id to the base model (SKillBase).

    Args:
        SkillBase (SkillBase): Base model of a skill
    """

    id: int

    class Config:
        """Configuration of the model.

        Activates the orm_mode of the pydantic model.
        """

        orm_mode = True
