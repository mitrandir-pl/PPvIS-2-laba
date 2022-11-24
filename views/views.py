from abc import ABC, abstractmethod
from enum import Enum

from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '720')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from models.models import Color


RED = [1, 0, 0, 1]
GREEN = [0, 1, 0, 1]
BLUE = [0, 0, 1, 1]
PURPLE = [1, 0, 1, 1]
GRAY = [1, 1, 1, 1]


class Drawing(ABC):
    x: int
    y: int
    xscale: int
    yscale: int
    depth: int

    @abstractmethod
    def draw(self):
        pass


class TextField(Drawing):
    text: str

    def draw(self):
        pass


class Button_(Drawing):

    def draw(self):
        pass


class Image(Drawing):
    data: bytes
    width: int
    height: int

    def draw(self):
        pass


class ButtonWithImage(Button):
    image: Image

    def draw(self):
        pass


class TextButton(Button):
    text: str

    def draw(self):
        pass


class ColorButton(Button):
    color: Color

    def draw(self):
        pass


class ApproveButton(Button):
    state: bool

    def draw(self):
        pass


class DrawingContainer(Drawing):
    objects: list[Drawing]

    def draw(self):
        pass


class ViewType(Enum):
    DAY = 1
    WEEK = 2
    MONTH = 3
    NOTE_WITHOUT_DATE = 4
    FILTER = 5
    CLEAR = 6


class Window(Screen):
    drawing: DrawingContainer
    views: dict[ViewType: DrawingContainer]
    curr_view: ViewType
    curr_view: DrawingContainer

    def __init__(self, **kw):
        super(Window, self).__init__(**kw)
        self.box_layout_notes1 = BoxLayout(orientation="vertical", padding=[40, 125, 0, 375])
        btn1 = Button(text='X текст записи', size_hint=(1, .1))
        btn2 = Button(text='X текст записи', size_hint=(1, .1))
        btn3 = Button(text='X текст записи', size_hint=(1, .1))
        btn4 = Button(text='+', size_hint=(1, .1))
        self.box_layout_notes1.add_widget(btn1)
        self.box_layout_notes1.add_widget(btn2)
        self.box_layout_notes1.add_widget(btn3)
        self.box_layout_notes1.add_widget(btn4)
        self.box_layout_notes2 = BoxLayout(orientation="vertical", padding=[40, 115, 0, 320])
        self.box_layout_groups = BoxLayout(orientation="horizontal", padding=[40, 30, 400, 485])
        btn1 = Button(text='Группа 1 Х', size_hint=(.3, 1))
        btn2 = Button(text='Группа 2 Х', size_hint=(.3, 1))
        btn3 = Button(text='Группа 3 Х', size_hint=(.3, 1))
        btn4 = Button(text='+', size_hint=(.3, 1))
        self.box_layout_groups.add_widget(btn1)
        self.box_layout_groups.add_widget(btn2)
        self.box_layout_groups.add_widget(btn3)
        self.box_layout_groups.add_widget(btn4)
        btn_group = Button(text='Группа 1', size_hint=(1, .1))
        btn1 = Button(text='X текст записи', size_hint=(1, .1))
        btn2 = Button(text='X текст записи', size_hint=(1, .1))
        btn3 = Button(text='X текст записи', size_hint=(1, .1))
        btn4 = Button(text='+', size_hint=(1, .1))
        self.box_layout_notes2.add_widget(btn_group)
        self.box_layout_notes2.add_widget(btn1)
        self.box_layout_notes2.add_widget(btn2)
        self.box_layout_notes2.add_widget(btn3)
        self.box_layout_notes2.add_widget(btn4)

        self.box_layout_notes3 = BoxLayout(orientation="vertical", padding=[40, 125, 0, 275])
        btn1 = Button(text='4 XXXXX', size_hint=(1, .1))
        btn2 = Button(text='5 XXXXX', size_hint=(1, .1))
        btn3 = Button(text='6 XXX', size_hint=(1, .1))
        btn4 = Button(text='7 X', size_hint=(1, .1))
        btn5 = Button(text='8 XXX', size_hint=(1, .1))
        btn6 = Button(text='9 XX', size_hint=(1, .1))
        btn7 = Button(text='10 ', size_hint=(1, .1))
        self.box_layout_notes3.add_widget(btn1)
        self.box_layout_notes3.add_widget(btn2)
        self.box_layout_notes3.add_widget(btn3)
        self.box_layout_notes3.add_widget(btn4)
        self.box_layout_notes3.add_widget(btn5)
        self.box_layout_notes3.add_widget(btn6)
        self.box_layout_notes3.add_widget(btn7)

        self.calendar = GridLayout(cols=7, padding=[80, 125, 0, 100])
        self.weeks = BoxLayout(orientation="vertical", padding=[40, 125, 720, 100])
        for i in range(19, 25):
            btn = Button(text=str(i))
            self.weeks.add_widget(btn)
        for i in range(26, 31):
            date = Button(text=str(i), disabled=True)
            self.calendar.add_widget(date)
        for i in range(1, 32):
            date = Button(text=str(i))
            self.calendar.add_widget(date)
        for i in range(1, 7):
            date = Button(text=str(i), disabled=True)
            self.calendar.add_widget(date)

        self.use_filters = BoxLayout(padding=[40, 125, 300, 450])
        use_filters_btn = Button(text="V", size_hint=(.1, 1))
        use_filters_txt = Button(text="Использовать фильтры?")
        self.use_filters.add_widget(use_filters_btn)
        self.use_filters.add_widget(use_filters_txt)

        self.filter_btns = BoxLayout(padding=[40, 150, 0, 420])
        use_filters_btn1 = Button(text="Вкл. Все")
        use_filters_btn2 = Button(text="Выкл. Все")
        use_filters_btn3 = Button(text="Вкл. Все")
        use_filters_btn4 = Button(text="Выкл. Все")
        self.filter_btns.add_widget(use_filters_btn1)
        self.filter_btns.add_widget(use_filters_btn2)
        self.filter_btns.add_widget(use_filters_btn3)
        self.filter_btns.add_widget(use_filters_btn4)

        self.icon_names = GridLayout(cols=6, padding=[40, 175, 0, 0])
        for i in range(14):
            btn = Button(text="V", size_hint=(.1, 1))
            btn2 = Button(text="X", size_hint=(.1, 1))
            btn1 = Button(text=": названиеИконки")
            self.icon_names.add_widget(btn)
            self.icon_names.add_widget(btn2)
            self.icon_names.add_widget(btn1)

        self.clear_btns = GridLayout(cols=3, padding=[40, 125, 300, 400])
        btn1 = Button(text="Начальная дата: ", size_hint=(.5, 1))
        btn2 = Button(text="1/1/1970", size_hint=(.4, 1))
        btn3 = Button(text="V", size_hint=(.1, 1))
        btn4 = Button(text="Конечная дата: ", size_hint=(.5, 1))
        btn5 = Button(text="5/1/1970", size_hint=(.4, 1))
        btn6 = Button(text="V", size_hint=(.1, 1))
        self.clear_btns.add_widget(btn1)
        self.clear_btns.add_widget(btn2)
        self.clear_btns.add_widget(btn3)
        self.clear_btns.add_widget(btn4)
        self.clear_btns.add_widget(btn5)
        self.clear_btns.add_widget(btn6)
        self.clear_box = BoxLayout(orientation="vertical", padding=[40, 200, 0, 300])
        btn = Button(text="Будут удалены записи с 1/1/1970 по 5/1/1970")
        btn1 = Button(text="(включительно с обеих сторон)")
        btn2 = Button(text="Очистить")
        self.clear_box.add_widget(btn)
        self.clear_box.add_widget(btn1)
        self.clear_box.add_widget(btn2)

        box_layout = BoxLayout(orientation="vertical", padding=[0, 0, 0, 200])
        button1 = Button(text="X", font_size=50, size_hint=(.05, .1), pos_hint={"x": 0})
        button2 = Button(text="X", font_size=50, size_hint=(.05, .1), pos_hint={"x": 0},
                         on_press=lambda x: self.draw(1))
        button3 = Button(text="X", font_size=50, size_hint=(.05, .1), pos_hint={"x": 0},
                         on_press=lambda x: self.draw(2))
        button4 = Button(text="X", font_size=50, size_hint=(.05, .1), pos_hint={"x": 0},
                         on_press=lambda x: self.draw(3))
        button5 = Button(text="X", font_size=50, size_hint=(.05, .1), pos_hint={"x": 0},
                         on_press=lambda x: self.draw(4))
        button6 = Button(text="X", font_size=50, size_hint=(.05, .1), pos_hint={"x": 0},
                         on_press=lambda x: self.draw(5))
        button7 = Button(text="X", font_size=50, size_hint=(.05, .1), pos_hint={"x": 0},
                         on_press=lambda x: self.draw(6))
        box_layout.add_widget(button1)
        box_layout.add_widget(button2)
        box_layout.add_widget(button3)
        box_layout.add_widget(button4)
        box_layout.add_widget(button5)
        box_layout.add_widget(button6)
        box_layout.add_widget(button7)
        box_layout1 = BoxLayout(orientation="horizontal", padding=[40, 0, 0, 585])
        button_way = Button(text='очень/длинный/путь/кежедневнику.tkjr',
                            font_size=20, size_hint=(.7, .1))
        button_create = Button(text='Cохранить',
                               font_size=20, size_hint=(.15, .1))
        button_load = Button(text='Загрузить',
                             font_size=20, size_hint=(.15, .1))
        box_layout1.add_widget(button_way)
        box_layout1.add_widget(button_create)
        box_layout1.add_widget(button_load)
        box_layout2 = BoxLayout(orientation="horizontal", padding=[40, 30, 0, 475])
        self.a = Button(background_color=[.85, .85, .85, 1])
        box_layout2.add_widget(self.a)
        self.add_widget(box_layout)
        self.add_widget(box_layout1)
        self.add_widget(box_layout2)

    def draw(self, a):
        match a:
            case 1:
                self.remove_widget(self.use_filters)
                self.remove_widget(self.filter_btns)
                self.remove_widget(self.icon_names)
                self.remove_widget(self.box_layout_groups)
                self.remove_widget(self.box_layout_notes1)
                self.remove_widget(self.box_layout_notes2)
                self.remove_widget(self.box_layout_notes3)
                self.remove_widget(self.calendar)
                self.remove_widget(self.weeks)
                self.remove_widget(self.clear_btns)
                self.remove_widget(self.clear_box)
                self.a.text = "< 1/1/1970"
                self.a.font_size = 30
                self.a.halign = 'left'
                self.add_widget(self.box_layout_notes1)
            case 2:
                self.remove_widget(self.box_layout_groups)
                self.remove_widget(self.box_layout_notes1)
                self.remove_widget(self.box_layout_notes2)
                self.remove_widget(self.box_layout_notes3)
                self.remove_widget(self.calendar)
                self.remove_widget(self.weeks)
                self.remove_widget(self.use_filters)
                self.remove_widget(self.filter_btns)
                self.remove_widget(self.icon_names)
                self.remove_widget(self.clear_btns)
                self.remove_widget(self.clear_box)
                self.a.text = ""
                self.add_widget(self.box_layout_groups)
                self.add_widget(self.box_layout_notes2)
            case 3:
                self.remove_widget(self.box_layout_groups)
                self.remove_widget(self.box_layout_notes1)
                self.remove_widget(self.box_layout_notes2)
                self.remove_widget(self.box_layout_notes3)
                self.remove_widget(self.calendar)
                self.remove_widget(self.weeks)
                self.remove_widget(self.use_filters)
                self.remove_widget(self.filter_btns)
                self.remove_widget(self.icon_names)
                self.remove_widget(self.clear_btns)
                self.remove_widget(self.clear_box)
                self.a.text = "< 4/1/1970 - 10/1/1970"
                self.a.font_size = 30
                self.add_widget(self.box_layout_notes3)
            case 4:
                self.remove_widget(self.box_layout_groups)
                self.remove_widget(self.box_layout_notes1)
                self.remove_widget(self.box_layout_notes2)
                self.remove_widget(self.box_layout_notes3)
                self.remove_widget(self.calendar)
                self.remove_widget(self.weeks)
                self.remove_widget(self.use_filters)
                self.remove_widget(self.filter_btns)
                self.remove_widget(self.icon_names)
                self.remove_widget(self.clear_btns)
                self.remove_widget(self.clear_box)
                self.a.text = ""
                self.add_widget(self.calendar)
                self.add_widget(self.weeks)

            case 5:
                self.remove_widget(self.box_layout_groups)
                self.remove_widget(self.box_layout_notes1)
                self.remove_widget(self.box_layout_notes2)
                self.remove_widget(self.box_layout_notes3)
                self.remove_widget(self.calendar)
                self.remove_widget(self.weeks)
                self.remove_widget(self.use_filters)
                self.remove_widget(self.filter_btns)
                self.remove_widget(self.icon_names)
                self.remove_widget(self.clear_btns)
                self.remove_widget(self.clear_box)
                self.a.text = "Фильтры"
                self.a.font_size = 30

                self.add_widget(self.use_filters)
                self.add_widget(self.filter_btns)
                self.add_widget(self.icon_names)

            case 6:
                self.remove_widget(self.box_layout_groups)
                self.remove_widget(self.box_layout_notes1)
                self.remove_widget(self.box_layout_notes2)
                self.remove_widget(self.box_layout_notes3)
                self.remove_widget(self.calendar)
                self.remove_widget(self.weeks)
                self.remove_widget(self.use_filters)
                self.remove_widget(self.filter_btns)
                self.remove_widget(self.icon_names)
                self.remove_widget(self.clear_btns)
                self.remove_widget(self.clear_box)
                self.a.text = "Очистка"
                self.a.font_size = 30
                self.add_widget(self.clear_btns)
                self.add_widget(self.clear_box)