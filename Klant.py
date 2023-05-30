import socket
import sys
import json

HOST, PORT = '192.168.100.57', 9090


klantorder = {"id": (str(input("wat is ID?"))), "name": (input("naam?"))}




# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(klantorder,encoding="utf-8"))


    # kan weg
    received = sock.recv(1024)
    received = received.decode("utf-8")

finally:
    sock.close()

print( "Sent:     {}".format(klantorder))
print ("Received: {}".format(received))
