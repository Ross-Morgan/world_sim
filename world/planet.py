from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Iterable, Iterator, Optional

from data.ids import SequentialID
from data.units import Size, Unit
from person import Person


class Population:
    def __init__(self, people: Iterable[Person] = None) -> None:
        if people is None:
            people = []

        self.people = people
        self.iterator = people

    def __iter__(self):
        self.iterator = iter(self.people)
        return self.iterator

    def __next__(self):
        return next(self.iterator)


@dataclass
class Planet:
    name: str
    id: int
    is_habitable: bool
    radius: Decimal
    population: int = 0
    people: Population = Population()


@dataclass
class SolarSystem:
    planets: Iterable[Planet]


@dataclass
class HabitablePlanet(Planet):
    is_habitable: bool = field(init=False)

    def __post_init__(self):
        self.is_habitable = True


if __name__ == "__main__":
    _distance = Unit.Distance.Units

    earth = HabitablePlanet(
        name="Earth",
        id=SequentialID().id,
        radius=Size(3959,  _distance.MI)
    )

    print(earth)
