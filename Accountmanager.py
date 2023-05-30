import socket
import sys
import json

HOST, PORT = '192.168.100.57' , 9090


#klantorder = {"client": "Accountmanager", "destClient": "", "MijnIP": HOST, "name": (input("naam?"))}

#data = json.dumps(klantorder)
#print(data)
# Create a socket (SOCK_STREAM means a TCP socket)
while True:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data

        sock.connect((HOST, PORT))
        #sock.sendall(bytes(data, encoding="utf-8"))


        received = sock.recv(1024)
        received = received.decode("utf-8")
    except:
        print("error")



print( "Sent:     {}".format(klantorder))
print ("Received: {}".format(received))
