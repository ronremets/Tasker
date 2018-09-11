# coding=ascii
"""
login form
"""
import socket
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from tools.command import Command
from tools.user import User
__author__ = "Ron Remets"


class LoginPopup(Popup):
    """
    popup
    """
    dismiss_button = ObjectProperty(None)
    text = ""


class LoginForm(Widget):
    """
    login form
    """

    def __init__(self, client):
        super(LoginForm, self).__init__()
        self._username_input = ObjectProperty(None)
        self._password_input = ObjectProperty(None)
        self._login_button = ObjectProperty(None)
        self._signup_button = ObjectProperty(None)
        self._client = client

    def login(self, username, password):
        self._client.write("login?username={}&password={}".format(
            username,
            password))
        data = self._client.read()
        command = Command(data)
        if command["error"] == '0':
            LoginPopup.text = command["info"]
            LoginPopup().open()
            return User(username, password, command["info"])
        else:
            LoginPopup.text = "Error logging in"
            LoginPopup().open()
            return None

    def signup(self, username, password, info):
        self._client.write("signup?username={}&password={}&info={}".format(
            username,
            password,
            info))
        data = self._client.read()
        command = Command(data)
        if command["error"] == '0':
            LoginPopup.text = info
            LoginPopup().open()
            return User(username, password, info)
        else:
            LoginPopup.text = "Error creating user"
            LoginPopup().open()
            return None
