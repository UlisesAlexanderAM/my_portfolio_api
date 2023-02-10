""" Module that defines the dataclass and functions related to skills. """

from typing import Any, Literal

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from sqlalchemy import Engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

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
        engine (Engine): Object Engine to access the DB
    """
    with Session(engine) as session:
        new_skill: Skill = Skill(skill_name=name, skill_level=level)
        session.add(new_skill)
        session.commit()
