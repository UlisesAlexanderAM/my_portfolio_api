#!/usr/bin/env python3
"""
Module that defines dataclass and functions related to
the job application/interest in a job or company
"""

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
from datetime import date

from skills import Skill


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


@dataclass
class Job:
    """
    Class that define a job application/interest in a company or job.

    Attributes:
        title (str): Title job of the job opening or job title interest.
        source (str): Source where the job opening came from or the interest company.
        date_of_application (Optional[date]): Date when the application was done or the resume sent.
        company_name (str): Name of the company the user is applying or is interested.
        skill (List[Skill]): List of skills related to the job opening.
        application_status (Status): Status in which the application is a the moment.
        skill_aligment (float): Value that indicate how prepared is the user for the job.

    TODO: decide how to calculate the skill aligment.
    """

    title: str
    source: str
    date_of_application: Optional[date]
    company_name: str
    skills: List[Skill]
    application_status: Status = Status.INTERESADO
    skill_aligment: float = field(init=False, repr=False)
