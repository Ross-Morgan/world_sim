from enum import Flag, auto


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
