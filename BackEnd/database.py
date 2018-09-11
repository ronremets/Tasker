# coding=ascii
"""
a database to store the tasks and users
"""
import sqlite3
import sys
from tools.user import User
from tools.task import Task

__author__ = "Ron Remets"


class Database(object):
    """
    a database class
    """

    def __init__(self, database_name):
        self._database = sqlite3.connect(database_name)
        self._cursor = self._database.cursor()
        try:
            self._create_tables()
        except Exception as e:
            sys.stderr.write("\nDATABASE ERROR:\n{}\n".format(e))
            if 'y' in input("Close db? (y/n)\n").lower():
                self.close()
                sys.exit(1)

    def _create_tables(self):
        self._cursor.executescript("""
CREATE TABLE Users(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
username VARCHAR(255) NOT NULL UNIQUE,
password VARCHAR(255) NOT NULL,
info TEXT);

CREATE TABLE Tasks(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(255) NOT NULL,
description TEXT,
deadline VARCHAR(255),
src_username VARCHAR(255) NOT NULL,
dst_username VARCHAR(255) NOT NULL,
complete VARCHAR(255) NOT NULL);
""")

    def close(self):
        self._database.close()

    def save(self):
        self._database.commit()

    def add_user(self, user):
        self._cursor.execute("""
INSERT INTO Users
(username, password, info)
VALUES
(?, ?, ?)
""", (user.get_username(), user.get_password(), user.get_info()))

    def add_task(self, task):
        self._cursor.execute("""
INSERT INTO Tasks
(name, description, deadline, src_username, dst_username, complete)
VALUES
(?, ?, ?, ?, ?, ?)
""", (
            task.get_name(),
            task.get_description(),
            task.get_deadline(),
            task.get_src_username(),
            task.get_dst_username(),
            str(task.get_complete())))

    def delete_user(self, username, password):
        self._cursor.execute("""
DELETE FROM Users
WHERE username = ? and password = ?
""", (username, password))

    def delete_task(self, user, task_id):
        self._cursor.execute("""
DELETE FROM Tasks
WHERE src_username = ? and id = ?
""", (user.get_username(), task_id))

    def get_user(self, username, password):
        self._cursor.execute("""
SELECT username, password, info FROM Users
WHERE username = ? and password = ?
""", (username, password))

        username, password, info = self._cursor.fetchone()
        return User(username, password, info)

    def get_tasks(self, user, *, src=True):
        tasks = []
        self._cursor.execute("""
SELECT name, description, deadline, src_username, dst_username, complete, id
FROM Tasks
WHERE {}_username = ?
""".format("src" if src else "dst"), (user.get_username(),))
        for task in self._cursor.fetchall():
            tasks.append(Task(*task))
        return tasks

    def get_task(self, user, task_id, *, src=True):
        self._cursor.execute("""
SELECT name, description, deadline, src_username, dst_username, complete, id
FROM Tasks
WHERE {}_username = ? and id = ?
""".format("src" if src else "dst"), (user.get_username(), task_id))
        task = self._cursor.fetchone()
        return Task(*task)

    def update_task(self, user, task):
        self._cursor.execute("""
UPDATE Tasks
SET
name = ?,
description = ?,
deadline = ?,
dst_username = ?,
complete = ?
WHERE
src_username = ? and id = ?
""", (
            task.get_name(),
            task.get_description(),
            task.get_deadline(),
            task.get_dst_username(),
            task.get_complete(),
            user.get_username(),
            task.get_id()))

    def update_user(self, user):
        self._cursor.execute("""
UPDATE Users
SET 
username = ?,
password = ?,
info = ?
WHERE
username = ? and password = ?
""", (
            user.get_username(),
            user.get_password(),
            user.get_info(),
            user.get_username(),
            user.get_password()))
