import socket

HOST = "192.168.100.57"
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello world".encode('utf-8'))
print(socket.recv(1024))
