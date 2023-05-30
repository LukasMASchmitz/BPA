import socket
import sys
import json

HOST, PORT = '192.168.100.57' , 9090

while True:
    klantorder = {"client": "Klant", "destClient": "Accountmanager", "MijnIP": HOST, "name": (input("naam?"))}

    data = json.dumps(klantorder)
    print(data)
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data,encoding="utf-8"))


        # kan weg
        received = sock.recv(1024)
        received = received.decode("utf-8")

    finally:
        print("verzonden")



sock.close()

print( "Sent:     {}".format(klantorder))
print ("Received: {}".format(received))
