""" Module that defines the dataclass and functions related to skills. """

from dataclasses import dataclass


@dataclass
class Skill:
    """
    This is a class to define what its a skill

    Attributes:
        name (str): Name of the skill.
        level (float): Level of profeciency of the skill.
    """

    name: str
    level: float


def obtain_name_stin(message: str) -> str:
    return input(message)


def obtain_level_stin(message: str) -> str:
    return input(message)
