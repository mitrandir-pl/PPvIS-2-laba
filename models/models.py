import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


@dataclass
class Color:
    r: int
    g: int
    b: int


class IconType(Enum):
    pass


@dataclass
class Note:
    icon: IconType
    color: Color
    text: str


@dataclass
class GroupOfNotes:
    notes: list[Note]


class Filter(ABC):

    @abstractmethod
    def filter(self, notes: list[Note] | GroupOfNotes) -> list[bool]:
        pass


class ColorFilter(Filter):
    color: Color

    def filter(self, note: Note) -> bool:
        pass


class IconFilter(Filter):
    icon: IconType

    def filter(self, note: Note) -> bool:
        pass


class FilterConfig:
    filters: list[Filter]
    filters_activities: list[bool]

    def filter(self, notes: list[Note] | GroupOfNotes) -> list[bool]:
        pass


@dataclass
class Diary:
    filter: FilterConfig
    notes: dict[datetime.date: GroupOfNotes]
    notes_without_date: dict[str: GroupOfNotes]

    def return_names_of_groups_of_notes_without_date(self) -> list[str]:
        pass

    def create_group_of_notes_without_date(self, name: str) -> GroupOfNotes:
        pass

    def return_group_of_notes_without_date(self, name: str) -> GroupOfNotes:
        pass

    def rename_group_of_notes_without_date(self, name: str, new_name: str) -> None:
        pass

    def delete_group_of_notes_without_date(self, name: str) -> None:
        pass

    def return_dates_of_notes(self) -> list[datetime.date]:
        pass

    def return_day_notes(self, day: datetime.date) -> GroupOfNotes:
        pass

    def create_group_of_notes_day(self, day: datetime.date) -> GroupOfNotes:
        pass

    def delete_group_of_notes_day(self, day: datetime.date) -> GroupOfNotes:
        pass

    def delete_notes_between_days(self, start_date: datetime.date,
                                  end_date: datetime.date) -> int:
        pass


class Loader:

    def save(self, path: str, diary: Diary) -> None:
        pass

    def load(self, path: str) -> Diary:
        pass
