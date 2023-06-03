""" Module that defines the dataclass and functions related to skills. """

from typing import Any, List, Literal, Tuple

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from sqlalchemy import Engine, Select, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from database import create_engine


class Skill(DeclarativeBase):
    """Class defining the skill table"""

    __tablename__ = "skill"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    level: Mapped[float]


def create_skill_table() -> None:
    """Funtion that create the skill table"""
    engine: Engine = create_engine()
    Skill.metadata.create_all(bind=engine)


class AskNameWidget(GridLayout):
    """Widget to ask for the skill name"""

    def __init__(self, message: str, **kwargs) -> None:
        super(AskNameWidget, self).__init__(**kwargs)
        self.cols: Literal[2] = 2
        self.skill_name_label: Label = Label(text=message)
        self.add_widget(self.skill_name_label)
        self.skill_name: TextInput = TextInput(multiline=False)
        self.add_widget(self.skill_name)


class AskLevelWidget(GridLayout):
    """Widget to ask for the skill level"""

    def __init__(self, message: str, **kwargs: Any) -> None:
        super(AskLevelWidget, self).__init__(**kwargs)
        self.cols: Literal[2] = 2
        self.skill_level_label: Label = Label(text=message)
        self.add_widget(self.skill_level_label)
        self.skill_level: TextInput = TextInput(multiline=False)
        self.add_widget(self.skill_level)


def save_skill(name: str, level: float, engine: Engine) -> None:
    """Function that save a skill in the DB

    Args:
        name (str): Name of the skill
        level (float): Level of the skill
        engine (Engine): Object Engine to access to the DB
    """
    with Session(engine) as session:
        new_skill: Skill = Skill(name=name, level=level)
        session.add(new_skill)
        session.commit()


def edit_name(old_name: str, new_name: str, engine: Engine) -> None:
    """Function that edits the name of the skill

    Args:
        old_name (str): Old name of the skill
        new_name (str): New name of the skill
        engine (Engine): Object Engine to access to the DB
    """
    with Session(engine) as session:
        skill: Skill = get_skill(old_name, engine)
        skill.name = new_name
        session.commit()


def update_level(skill_name: str, new_level: float, engine: Engine) -> None:
    """Function that updates the level of the skill

    Args:
        skill_name (str): Name of the skill which level will be updated
        new_level (float): Value of the new skill level
        engine (Engine): Object Engine to access to the DB
    """
    with Session(engine) as session:
        skill: Skill = get_skill(skill_name, engine)
        skill.level = new_level
        session.commit()


def delete_skill(skill_name: str, engine: Engine) -> None:
    """Function that deletes a skill

    Args:
        skill_name (str): Name of the skill to be deleted
        engine (Engine): Object Engine to access to the DB
    """
    with Session(engine) as session:
        skill: Skill = get_skill(skill_name, engine)
        session.delete(skill)
        session.flush()
        session.commit()


def get_skill(skill_name: str, engine: Engine) -> Skill:
    """Function that retrieves a skill from the database

    Args:
        skill_name (str): Name of the skill
        skill_level (float): Level of the skill
        engine (Engine): Object Engine to access to the DB

    Returns:
        Skill: _description_
    """
    with Session(engine) as session:
        stmt: Select[Tuple[Skill]] = select(Skill).where(Skill.name == skill_name)
        skill: Skill = session.scalars(stmt).one()
        return skill


def get_all_skills(engine: Engine) -> List[Skill]:
    """Function that returns a list with all the skills

    Args:
        engine (Engine): Object Engine to access to the DB

    Returns:
        list[Tuple[str, float]]: List of skills
    """
    with Session(engine) as session:
        stmt: Select[Tuple[str, float]] = select(Skill.name, Skill.level)
        skills: List[Skill] = []
        for skill in session.scalars(stmt):
            skills.append(skill)
        return skills
