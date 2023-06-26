"""Module that stores the Pydantic models/schemas"""

from pydantic import BaseModel, Field


class SkillBase(BaseModel):
    name: str = Field(max_length=30)
    level: float = Field(ge=0, le=1)


class SkillCreate(SkillBase):
    pass


class Skill(SkillBase):
    id: int

    class Config:
        orm_mode = True
