"""Pydantic schemas/models.

The models are used for FastAPI to perform validations,
and generate documentation.
"""

import pydantic


class SkillBase(pydantic.BaseModel):
    """Base model/schema for skill.

    Representation:
    - name(str): Skill name
    - level(float): Skill level. 0 < level < 1
    """

    name: str
    level: float = pydantic.Field(ge=0, le=1)


class SkillCreate(SkillBase):
    """Model representing the data needed to create a skill in the DB (Is the same a SkillBase).

    Representation:
    - name(str): Skill name
    - level(float): Skill level. 0 < level < 1
    """

    pass


class Skill(SkillBase):
    """Model representing the skill in the database.

    This models adds the id to the base model (SKillBase).

    Final representation:
    - name(str): Skill name
    - level(float): Skill level. 0 < level < 1
    - id(int): Skill ID. Exclusive of the database

    Args:
        SkillBase: Base model of a skill
    """

    id: int

    class Config:
        """Configuration of the model.

        Activates the orm_mode of the pydantic model.
        """

        orm_mode = True
