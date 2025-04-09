import enum
from typing import Iterable

class WeekDay(enum.IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    @classmethod
    def get_weekday_number(cls, week_day_str: str): ...
    @classmethod
    def convert(cls, day: str | WeekDay) -> int: ...
    @classmethod
    def validate_week_day(cls, week_day: str | WeekDay | Iterable[str] | Iterable[WeekDay]) -> set[int]: ...
