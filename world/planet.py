from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Iterable

from data.ids import SequentialID
from data.units import Size, Unit


@dataclass
class Planet:
    name: str
    id: int
    is_habitable: bool
    radius: Decimal

@dataclass
class SolarSystem:
    planets: Iterable[Planet]


@dataclass
class HabitablePlanet(Planet):
    is_habitable: bool = field(init=False)

    def __post_init__(self):
        self.is_habitable = True


def main():
    _distance = Unit.Distance.Units

    earth = HabitablePlanet(
        name="Earth",
        id=SequentialID().id,
        radius=Size(3959,  _distance.MI)
    )

    print(earth)


if __name__ == "__main__":
    main()
