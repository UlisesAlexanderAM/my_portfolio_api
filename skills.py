#!/usr/bin/env python3
""" Module that defines the dataclass and functions related to skills. """

from dataclasses import dataclass

from kivy.app import App
from kivy.uix.label import Label


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


def obtain_name_kivy_label(message: str):
    return Label(text=message)
