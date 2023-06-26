"""Module that defines the routes related to skills."""

from typing import Annotated

import fastapi as fa
from fastapi import status
from fastapi import responses
from sqlalchemy import orm

from app import crud
from app import dependencies as deps
from app.models import schemas, models

skills = fa.APIRouter(
    prefix="/skills",
    tags=["skills"],
    responses={404: {"description": "Skill not found"}},
)


@skills.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Retrieve all the skills",
    response_model=list[schemas.Skill],
)
def get_skills(
    db: Annotated[orm.Session, fa.Depends(deps.get_db)]
) -> list[models.Skill]:
    """Retrieve the skills from the database.

    Args:
        db: Manages all the operations

    Returns:
        List of skills
    """
    return crud.get_skills(db=db)


@skills.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="Add/save a skill",
    response_class=responses.JSONResponse,
)
def add_skill(
    skill: Annotated[
        schemas.SkillCreate, fa.Query(description="Skill to add to the DB")
    ],
    db: Annotated[orm.Session, fa.Depends(deps.get_db)],
):
    crud.save_skill(db=db, skill=skill)
    return {"message": "Skill added successfully"}


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


# def update_level(skill_name: str, new_level: float, engine: Engine) -> None:
#     """Function that updates the level of the skill

#     Args:
#         skill_name (str): Name of the skill which level will be updated
#         new_level (float): Value of the new skill level
#         engine (Engine): Object Engine to access to the DB
#     """
#     with Session(engine) as session:
#         skill: Skill = get_skill(skill_name, engine)
#         skill.level = new_level
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


# def get_skill(skill_name: str, engine: Engine) -> Skill:
#     """Function that retrieves a skill from the database

#     Args:
#         skill_name (str): Name of the skill
#         skill_level (float): Level of the skill
#         engine (Engine): Object Engine to access to the DB

#     Returns:
#         Skill: _description_
#     """
#     with Session(engine) as session:
#         stmt: Select[Tuple[Skill]] = select(Skill).where(Skill.name == skill_name)
#         skill: Skill = session.scalars(stmt).one()
#         return skill
