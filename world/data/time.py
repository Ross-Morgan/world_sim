from dataclasses import dataclass
from enum import Enum

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


@dataclass
class Date:
    year: int
    month: int
    day: int

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    def phonetic(self) -> str:
        return f""


@dataclass
class Time:
    hour: int
    minute: int
    second: int

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    def phonetic(self) -> str:
        return f""


@dataclass
class DateTime(Time, Date):
    def __str__(self):
        date = Date(self.year, self.month, self.day)
        time = Time(self.hour, self.minute, self.second)

        return f"{date}T{time}"


date = Date(2022, 1, 9)
time = Time(0, 34, 0)
datetime = DateTime(2022, 1, 9, 0, 34, 0)

print(date)
print(time)
print(datetime)