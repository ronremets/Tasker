# coding=ascii
"""
main form
"""
import socket
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from command import Command
__author__ = "Ron Remets"


class MainForm(Widget):
    """
    main form
    """
    connect_button = ObjectProperty(None)
    info_label = ObjectProperty(None)
    close_button = ObjectProperty(None)

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
