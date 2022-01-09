from enum import Enum, auto

class _AutoName(Enum):
    def _generate_next_value_(self, *args):
        name: str = self
        return name.title()


class Biology:
    class Sex(_AutoName):
        MALE = auto()
        FEMALE = auto()
        INTERSEX = auto()


class Qualification:
    class Education(_AutoName):
        UNEDUCATED = auto()

        PRIMARY = auto()
        SECONDARY = auto()
        HIGHER = auto()
        MASTERS = auto()
        DOCTORATE = auto()

    class JobStatus(_AutoName):
        UNEMPLOYED = auto()

        SELF_EMPLOYED = auto()
        EMPLOYED = auto()
