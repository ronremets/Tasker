# coding=ascii
"""
main app
"""
from kivy.app import App
from main_form import MainForm
from login_form import LoginForm
from client import Client
__author__ = "Ron Remets"


class TaskerApp(App):
    """
    main app
    """
    client = None
    def build(self):
        TaskerApp.client = Client("127.0.0.1", 2125)
        return LoginForm(TaskerApp.client)


TaskerApp().run()
if TaskerApp.client is not None:
    print("Closing...")
    TaskerApp.client.write("close?")
    TaskerApp.client.close()

"""
signup?username=ronremets&password=12345&info=me
login?username=ronremets&password=12345
add task?username=ronremets&password=12345&name=clean2&description=clean2 the house&deadline=now&add task?name=clean&description=clean the house&deadline=now&dst_username=nirremets&complete=False
get task?username=ronremets&password=12345&src=True
"""
