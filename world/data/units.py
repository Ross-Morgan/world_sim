from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
from enum import Enum, auto
from typing import Final


class _AutoName(Enum):
    def _generate_next_value_(*args):
        return args[0]


class Unit:
    class Distance:
        _conversions: Final[dict[str, Decimal]] = {
            "KM": Decimal(1),
            "MI": Decimal(1.609344),
            "NM": Decimal(1.852),
        }

        class Units(_AutoName):
            KM = "KM"
            MI = "MI"
            NM = "NM"
            AU = "AU"
            LY = "LY"

        @classmethod
        def convert(cls, value: Decimal, unit1: Unit.Distance.Units, unit2: Unit.Distance.Units):
            return cls._conversions.get()


    class Temperature(_AutoName):
        pass


class Size:
    def __init__(self, value: float | Decimal, unit: Unit.Distance.Units):
        self.value = Decimal(value)
        self.unit = unit

    def __str__(self) -> str:
        return f"{str(self.value)} {self.unit.name}"

    def __repr__(self) -> str:
        return f"'{str(self)}'"

    def __mul__(self, other: Decimal):
        return self.__class__(self.value * other, self.unit)
