# coding=ascii
"""
a user
"""
__author__ = "Ron Remets"


class User(object):
    """
    a user class
    """

    def __init__(self, username, password, info):
        self._username = username
        self._password = password
        self._info = info

    def __str__(self):
        return """\
username = {}
password = {}
info = {}
""".format(self._username, self._password, self._info)

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_info(self):
        return self._info

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_info(self, info):
        self._info = info
