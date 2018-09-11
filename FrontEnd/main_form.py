# coding=ascii
"""
main form
"""
import socket
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from tools.command import Command
__author__ = "Ron Remets"


class MainForm(Widget):
    """
    main form
    """

    def __init__(self, client):
        super(MainForm, self).__init__()
        self._connect_button = ObjectProperty(None)
        self._info_label = ObjectProperty(None)
        self._close_button = ObjectProperty(None)
        self._client = client

    def connect(self):
        client = socket.socket()
        try:
            client.connect(("127.0.0.1", 2125))
            client.send(b"signup?username=ronremets&password=12345&info=me")
            print(str(client.recv(1024)))
            client.send(b"login?username=ronremets&password=12345")
            self.info_label.text = \
                Command(str(client.recv(1024))[2:-1])["info"]
            print("done")
        finally:
            client.close()
