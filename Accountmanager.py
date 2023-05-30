import socket

#HOST = "192.168.100.57"
PORT = 9090
HOST = socket.gethostname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)