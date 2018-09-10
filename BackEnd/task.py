# coding=ascii
"""
a task
"""
__author__ = "Ron Remets"


class Task(object):
    """
    a task class
    """

    def __init__(self,
                 name,
                 description,
                 deadline,
                 src_username,
                 dst_username,
                 complete):
        self._name = name
        self._description = description
        self._deadline = deadline
        self._src_username = src_username
        self._dst_username = dst_username
        self._complete = complete

    def __str__(self):
            return """\
name = {}
description = {}
deadline = {}
src_username = {}
dst_username = {}
complete = {}
""".format(
                self._name,
                self._description,
                self._deadline,
                self._src_username,
                self._dst_username,
                self._complete)

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_deadline(self):
        return self._deadline

    def get_src_username(self):
        return self._src_username

    def get_dst_username(self):
        return self._dst_username

    def get_complete(self):
        return self._complete

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description

    def set_deadline(self, deadline):
        self._deadline = deadline

    def set_src_username(self, src_username):
        self._src_username = src_username

    def set_dst_username(self, dst_username):
        self._dst_username = dst_username

    def set_complete(self, complete):
        self._complete = complete
