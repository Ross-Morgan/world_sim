from enum import Enum, Flag, auto


class PoliticalIndex(Flag):
    LEFT = auto()
    RIGHT = auto()
    AUTH = auto()
    LIB = auto()
    CENTRE = auto()


class PoliticalParty:
    def __init__(self, name: str, position: PoliticalIndex):
        self.name = name
        self.position = position

    def __str__(self):
        return self.name


class ElectoralSystems(Enum):
    # Plurality
    FIRST_PAST_THE_POST = auto()
    PLURALITY_AT_LARGE = auto()
    GENERAL_TICKET = auto()

    # Majority
    TWO_ROUND = auto()
    INSTANT_RUNOFF = auto()

    # Semi-proportional
    SINGLE_NON_TRANSFERABLE_VOTE = auto()
    CUMULATIVE = auto()
    BINOMIAL = auto()

    # Proportional
    PARTY_LIST_PROP_REP = auto()
    SINGLE_TRANSFERABLE_VOTE = auto()

    # Mixed
    MAJORITY_BONUS = auto()
    MIXED_MEMBER_PROP_REP = auto()
    MIXED_MEMBER_MAJ_REP = auto()

    # Other
    BORDA = auto()
