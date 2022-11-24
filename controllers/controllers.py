from abc import ABC, abstractmethod
from datetime import date

from models.models import Diary, Loader, Color, IconType, Filter
from views.views import ViewType


class ViewHandler(ABC):

    @abstractmethod
    def when_starts(self) -> None:
        pass


class WeekViewHandler(ViewHandler):

    def when_starts(self) -> None:
        pass

    def  when_go_to_next(self) -> None:
        pass

    def when_go_to_past(self) -> None:
        pass

    def when_day_pressed(self, day: date) -> None:
        pass


class DayViewHandler(ViewHandler):

    def when_starts(self) -> None:
        pass

    def when_note_created(self) -> None:
        pass

    def when_go_to_next(self) -> None:
        pass

    def when_go_to_past(self) -> None:
        pass

    def when_icon_pressed(self, note_id: int) -> None:
        pass

    def when_color_pressed(self, note_id: int) -> None:
        pass

    def when_text_changed(self, note_id: int) -> None:
        pass


class FilterViewHandler(ViewHandler):

    def when_starts(self) -> None:
        pass

    def when_filter_activity_changed(self, filter_id: int) -> None:
        pass


class CleaningViewHandler(ViewHandler):
    start_date: date
    end_date: date
    use_start_date: bool
    use_end_date: bool

    def when_starts(self) -> None:
        pass

    def when_delets(self) -> None:
        pass


class MonthViewHandler(ViewHandler):

    def when_starts(self) -> None:
        pass

    def when_go_to_next(self) -> None:
        pass

    def when_go_to_past(self) -> None:
        pass

    def when_week_pressed(self, week: date) -> None:
        pass

    def when_day_pressed(self, day: date) -> None:
        pass


class NotesWithoutDatesViewHandler(ViewHandler):

    def when_starts(self) -> None:
        pass

    def when_group_creates(self, group_name: str) -> None:
        pass

    def when_group_deletes(self, group_name: str) -> None:
        pass

    def when_group_opens(self, group_name: str) -> None:
        pass

    def when_group_renames(self, group_name: str) -> None:
        pass

    def when_note_created(self):
        pass

    def when_icon_pressed(self, note_id: int) -> None:
        pass

    def when_color_pressed(self, note_id: int) -> None:
        pass

    def when_text_changed(self, note_id: int) -> None:
        pass


class MainHandler:
    view_handler: dict[ViewType: ViewHandler]
    current_view: ViewType
    day: date


class TranslatorToNames:
    color_name: dict[Color: str]
    icon_names: dict[IconType: str]

    def icon_type_to_name(self, icon_type: IconType) -> str:
        pass

    def color_to_name(self, color: Color) -> str:
        pass

    def filterViewHandler(self, filter: Filter) -> str:
        pass


class Intermediary:
    diary: Diary
    loader: Loader
    main_handler: MainHandler
    translator: TranslatorToNames
