"""Module that defines the routes related to skills."""

from collections.abc import Sequence

import fastapi as fa
from fastapi import status

from app.data import crud
from app.models import models

router_skills = fa.APIRouter(
    prefix="/skills",
    tags=["skills"],
    responses={404: {"description": "Skill not found"}},
)


@router_skills.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Retrieve all the skills",
    response_model=Sequence[models.Skills],
)
def get_skills() -> Sequence[models.Skills]:
    """Retrieve the skills from the database.

    Args:
        db: Manages all the operations

    Returns:
        List of skills
    """
    return crud.get_skills()


@router_skills.get(
    path="/name/{skill_name}",
    status_code=status.HTTP_200_OK,
    summary="Retrieve all the skills",
    response_model=models.Skills,
)
def get_skill_by_name(skill_name: str) -> models.Skills | None:
    """Retrieve a skill from the database by its name.

    Args:
        skill_name: Name of the skill to retrieve
        db: Manages all the operations

    Returns:
        Skill with the given name
    """
    return crud.get_skill_by_name(skill_name)
