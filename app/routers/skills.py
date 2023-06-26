"""Module that defines the routes related to skills."""

from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import crud
from app.dependencies import get_db
from app.models import schemas

skills = APIRouter(
    prefix="/skills",
    tags=["skills"],
    responses={404: {"description": "Skill not found"}},
)


@skills.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="Add/save a skill",
    response_class=JSONResponse,
)
def add_skill(
    skill: Annotated[schemas.SkillCreate, Query(description="Skill to add to the DB")],
    db: Annotated[Session, Depends(get_db)],
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


# def get_all_skills(engine: Engine) -> List[Skill]:
#     """Function that returns a list with all the skills

#     Args:
#         engine (Engine): Object Engine to access to the DB

#     Returns:
#         list[Tuple[str, float]]: List of skills
#     """
#     with Session(engine) as session:
#         stmt: Select[Tuple[str, float]] = select(Skill.name, Skill.level)
#         skills: List[Skill] = []
#         for skill in session.scalars(stmt):
#             skills.append(skill)
#         return skills
