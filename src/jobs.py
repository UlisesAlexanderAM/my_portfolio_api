"""
Module that defines dataclass and functions related to
the job application/interest in a job or company
"""

from typing import List, Optional
from enum import Enum
from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from skills import Skill
from database import create_engine


class Status(Enum):
    """
    Class that defines an enumeration of the posible job application status.

    Attributes:
        INTERESADO: Spanish for interested
        PREPARANDO_PERSONALIZANDO_CV: Spanish for preparing/personalizing resume
        CV_ENVIADO_APPLICACION_INICIADA: Spanish for resume sent/application initiated
        AGENDANDO_ENTREVISTA: Spanish for scheduling interview
        ENTREVISTA_AGENDADA: Spanish for interview scheduled
        ACEPTADO: Spanish for accepted
        CONTRATO_FIRMADO: Spanish for contract signed
        ONBOARDING: Onborading in process
        RECHAZADO: Spanish for rejected

    """

    INTERESADO = 0
    PREPARANDO_PERSONALIZANDO_CV = 1
    CV_ENVIADO_APPLICACION_INICIADA = 2
    AGENDANDO_ENTREVISTA = 3
    ENTREVISTA_AGENDADA = 4
    ACEPTADO = 5
    CONTRATO_FIRMADO = 6
    ONBOARDING = 7
    RECHAZADO = 8


class Job(DeclarativeBase):
    """Class that define a job application/interest in a company or job

    Attributes:
        title (str): Title job of the job opening or job title interest.
        source (str): Source where the job opening came from or the interest company.
        date_of_application (Optional[date]): Date when the application was done or the resume sent.
        company_name (str): Name of the company the user is applying or is interested.
        skill (List[Skill]): List of skills related to the job opening.
        application_status (Status): Status in which the application is a the moment.
        skill_aligment (float): Value that indicate how prepared is the user for the job.Args:
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    source: Mapped[str]
    date_of_application: Mapped[Optional[date]]  # TODO implement dates with sqlalchemy
    company_name: Mapped[str]
    skills: Mapped[List["Skill"]] = relationship()
    application_status: Mapped[Status]  # TODO implement enums with sqlalchemy
    skill_aligment: Mapped[
        float
    ]  # TODO implement dataclass field(init=False, repr=False) into sqlalchemy


def create_jobs_table() -> None:
    """Funtion that create the skill table"""
    engine = create_engine()
    Job.metadata.create_all(engine)
