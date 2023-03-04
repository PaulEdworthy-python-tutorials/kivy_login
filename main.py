import os

from kaki.app import App
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.factory import Factory

# TO RUN IN TERMINAL TYPE, 'DEBUG=1 python main.py


class MainApp(App, MDApp):

    # set back to 0 to stop live reloading
    DEBUG = 1
    Window.size = [350, 660]

    # kivy files to watch
    KV_FILES = [
        os.path.join(os.getcwd(), 'screen_manager.kv'),
        os.path.join(os.getcwd(), 'login_screen.kv')
    ]

    # python files to watch
    CLASSES = {
        "MainScreenManager": "screen_manager",
        "LoginScreen": "login_screen"
    }

    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True})]

    def build_app(self):
        return Factory.MainScreenManager()


if __name__ == "__main__":
    MainApp().run()
