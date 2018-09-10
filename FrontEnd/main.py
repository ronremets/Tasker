# coding=ascii
"""
main app
"""
from kivy.app import App
from main_form import MainForm
__author__ = "Ron Remets"

class taskerApp(App):
    """
    main app
    """

    def build(self):
        return MainForm()

taskerApp().run()
