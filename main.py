from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from views.views import Window


screen_manager = ScreenManager()
screen_manager.add_widget(Window())


def set_screen(screen_name):
    screen_manager.current = screen_name


class TheLabApp(App):

    def build(self):
        Window.clearcolor = (.5, .5, .5, 1)
        return screen_manager


if __name__ == '__main__':
    TheLabApp().run()
