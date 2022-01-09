from dataclasses import dataclass, field

from data.lifeforms.humans import Biology, Qualification
from data.time import Date


@dataclass
class Person():
    """Representation of Person"""
    name: str
    age: int
    sex: Biology.Sex
    birth_date: Date
    education: Qualification.Education
    job_status: Qualification.JobStatus


@dataclass
class Male(Person):
    sex: Biology.Sex = field(init=False)

    def __post_init__(self):
        self.sex = Biology.Sex.MALE


@dataclass
class Female(Person):
    sex: Biology.Sex = field(init=False)

    def __post_init__(self):
        self.sex = Biology.Sex.FEMALE
