# coding=ascii
"""
server
"""
import socket
__author__ = "Ron Remets"
NUM_OF_CONNECTIONS = 5


class Server(object):
    """
    a server
    """

    def __init__(self, ip, port):
        self._server_socket = socket.socket()
        self._server_socket.bind((ip, port))
        self._server_socket.listen(NUM_OF_CONNECTIONS)
        self._client, self._address = self._server_socket.accept()

    def read(self):
        data = str(self._client.recv(1024))
        while len(data) <= 3:
            data = str(self._client.recv(1024))
        data = data[2:-1]
        print("data = <{}>".format(str([ord(i) for i in data])))
        return data

    def write(self, text):
        self._client.send(bytes(text, "US-ASCII"))
        print("Server Wrote:\n{}".format(text))

    def close(self):
        self._client.close()
        self._server_socket.close()
