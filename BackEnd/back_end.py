# coding=ascii
"""
this will manage everything to do with the backEnd
TODO: add better description
"""
import sys
from user import User
from task import Task
from database import Database
from server import Server
from command import Command

__author__ = "Ron Remets"
SERVER_IP = "0.0.0.0"
SERVER_PORT = 2125


class BackEnd(object):
    """
    a class to keep track of the backend
    TODO: add better description
    """

    def __init__(self, database_name, server_ip, server_port):
        self._database = Database(database_name)
        self._server = Server(server_ip, server_port)

    def run(self):
        while True:
            raw_command = self._server.read()
            command = Command(raw_command)
            print("\nCommand:\n" + str(command))
            command_output = self._execute(command)
            self._server.write(command_output)

    def close(self):
        self._database.close()

    def _execute(self, command):
        output = ""
        if command["command"] == "signup":
            output = repr(self._signup(command))
        elif command["command"] == "login":
            output = repr(self._login(command))
        elif command["command"] == "add task":
            output = repr(self._add_task(command))
        elif command["command"] == "get task":
            output = repr(self._get_all_tasks(command))
        return output

    def _signup(self, args):
        username = args["username"]
        password = args["password"]
        info = args["info"]
        user = User(username, password, info)
        self._database.add_user(user)
        return Command("end?error=0")

    def _login(self, args):
        user = self._database.get_user(args["username"], args["password"])
        return Command("end?error=0&info={}".format(user.get_info()))

    def _add_task(self, args):
        if self._login(args)["error"] == '0':
            task = Task(
                args["name"],
                args["description"],
                args["deadline"],
                args["username"],
                args["dst_username"],
                args["complete"])
            self._database.add_task(task)
            return Command("end?error=0")
        else:
            return Command("end?error=1")

    def _get_all_tasks(self, args):
        if self._login(args)["error"] == '0':
            tasks = self._database.get_tasks(
                self._database.get_user(args["username"], args["password"]),
                src=bool(args["src"]))
            return Command("end?error=0" + Command.iter_parse_task(tasks))
        else:
            return Command("end?error=1")


b = None
try:
    b = BackEnd(":memory:", SERVER_IP, SERVER_PORT)
    b.run()
except Exception as e:
    if b is not None:
        b.close()
    raise
"""
signup?username=ronremets&password=12345&info=me
login?username=ronremets&password=12345
add task?username=ronremets&password=12345&name=clean2&description=clean2 the house&deadline=now&add task?name=clean&description=clean the house&deadline=now&dst_username=nirremets&complete=False
get task?username=ronremets&password=12345&src=True
"""
