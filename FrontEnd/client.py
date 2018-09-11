# coding=ascii
"""
client
"""
import socket
RATE = 1024


class Client(object):
    """
    client
    """

    def __init__(self, server_ip, server_port):
        self._client_socket = socket.socket()
        try:
            self._client_socket.connect((server_ip, server_port))
        except Exception:
            self._client_socket.close()
            raise

    def read(self):
        data = str(self._client_socket.recv(RATE))
        print("DATA: " + data)
        if data.startswith("b'") and data.endswith("'"):
            return str(data)[2:-1]
        else:
            return str(data)

    def write(self, data):
        self._client_socket.send(bytes(data, "ascii"))

    def close(self):
        self._client_socket.close()
