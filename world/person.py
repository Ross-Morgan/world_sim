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


p = Person("Giga Chad", 69, Biology.Sex.INTERSEX, Date(420, 6, 9), Qualification.Education.DOCTORATE, Qualification.JobStatus.SELF_EMPLOYED)  # noqa
m = Male("Ross Morgan", 14, Date(2007, 3, 23), Qualification.Education.SECONDARY, Qualification.JobStatus.UNEMPLOYED)  # noqa
f = Female("Jane Doe", 30, Date(1992, 1, 9), Qualification.Education.HIGHER, Qualification.JobStatus.EMPLOYED)  # noqa


if __name__ == "__main__":
    print(p)
    print(m)
    print(f)
