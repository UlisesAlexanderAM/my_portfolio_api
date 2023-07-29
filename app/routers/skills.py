"""Module that defines the routes related to skills."""

from collections.abc import Sequence
from typing import Annotated

import fastapi as fa
from fastapi import responses, status
from sqlalchemy import orm

from app.data import crud
from app.data import dependencies as deps
from app.models import models, schemas

router_skills = fa.APIRouter(
    prefix="/skills",
    tags=["skills"],
    responses={404: {"description": "Skill not found"}},
)


@router_skills.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Retrieve all the skills",
    response_model=Sequence[schemas.Skill],
)
def get_skills(
    db: Annotated[orm.Session, fa.Depends(deps.get_db)]
) -> Sequence[models.Skill]:
    """Retrieve the skills from the database.

    Args:
        db: Manages all the operations

    Returns:
        List of skills
    """
    return crud.get_skills(db=db)


@router_skills.get(
    path="/name/{skill_name}",
    status_code=status.HTTP_200_OK,
    summary="Retrieve all the skills",
    response_model=schemas.Skill,
)
def get_skill_by_name(
    skill_name: str, db: Annotated[orm.Session, fa.Depends(deps.get_db)]
) -> models.Skill | None:
    """Retrieve a skill from the database by its name.

    Args:
        skill_name: Name of the skill to retrieve
        db: Manages all the operations

    Returns:
        Skill with the given name
    """
    return crud.get_skill_by_name(db, skill_name)


@router_skills.put(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="Add/save a skill",
    response_class=responses.JSONResponse,
)
def add_skill(
    skill: Annotated[
        schemas.SkillCreate, fa.Body(description="Skill to add to the DB")
    ],
    db: Annotated[orm.Session, fa.Depends(deps.get_db)],
):
    """Add a skill to the database.

    Args:
        db: Manages all the operations
        skill: Skill to add to the database.

    Raises:
        fa.HTTPException: The skill already exists in the database

    Returns:
        Message indicating that the skill was added successfully
    """
    if not crud.get_skill_by_name(db, skill_name=skill.name):
        crud.save_skill(db=db, skill=skill)
        return {"message": "Skill added successfully"}
    raise fa.HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Skill already added"
    )
