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


@router_skills.post(
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
        fa.HTTPException: If the skill already exists in the database

    Returns:
        Message indicating that the skill was added successfully
    """
    if not crud.get_skill_by_name(db, skill_name=skill.name):
        crud.save_skill(db=db, skill=skill)
        return {"message": "Skill added successfully"}
    raise fa.HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Skill already added"
    )


# def edit_name(old_name: str, new_name: str, engine: Engine) -> None:
#     """Function that edits the name of the skill

#     Args:
#         old_name (str): Old name of the skill
#         new_name (str): New name of the skill
#         engine (Engine): Object Engine to access to the DB
#     """
#     with Session(engine) as session:
#         skill: Skill = get_skill(old_name, engine)
#         skill.name = new_name
#         session.commit()


# def delete_skill(skill_name: str, engine: Engine) -> None:
#     """Function that deletes a skill

#     Args:
#         skill_name (str): Name of the skill to be deleted
#         engine (Engine): Object Engine to access to the DB
#     """
#     with Session(engine) as session:
#         skill: Skill = get_skill(skill_name, engine)
#         session.delete(skill)
#         session.flush()
#         session.commit()
