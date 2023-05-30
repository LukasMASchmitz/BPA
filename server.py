import socket
import os
from _thread import *
import json

ServerSideSocket = socket.socket()
host = '192.168.100.57'
port = 9090
ThreadCount = 0

#zodat server naar andere afdelingen kan sturen
global KlantIp
global PlanningIP
global AccountmanagerIP
global ProductieIP
global VoorraadIP

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Server is gestart..')
ServerSideSocket.listen(5)

#iedere verbonde afdeling creert een nieuwe van deze
def multi_threaded_client(connection):
    connection.send(str.encode('Ontvangen'))
    while True:
        data = connection.recv(1024)
        data = data.decode('utf-8') #decodeerd
        data = json.loads(data) #convert naar json
        print(data)

        #volgende elifs zijn alleen om de Ip op te slaan
        if data["client"] == "Klant":
            KlantIP = data["MijnIP"]
            print("KlantIP is: "+ KlantIP)
        elif data["client"] == "Planning":
            PlanningIP = data["MijnIP"]
            print("PlanningIP is: " + PlanningIP)
        elif data["client"] == "Accountmanager":
            AccountmanagerIP = data["MijnIP"]
            print("PlanningIP is: " + AccountmanagerIP)
        elif data["client"] == "Productie":
            ProductieIP = data["MijnIP"]
            print("ProductieIP is: " + ProductieIP)
        elif data["client"] == "Voorraad":
            VoorraadIP = data["MijnIP"]
            print("VoorraadIP is: " + VoorraadIP)


        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # volgende elifs zijn om data naar destination te sturen
        if data["destClient"] == "Accountmanager":
            sock.connect(AccountmanagerIP, 9090)
            sock.sendall(bytes(data, encoding="utf-8"))
        elif data["destClient"] == "Klant":
            sock.connect(KlantIP, 9090)
            sock.sendall(bytes(data, encoding="utf-8"))
        elif data["destClient"] == "Planning":
            sock.connect(PlanningIP, 9090)
            sock.sendall(bytes(data, encoding="utf-8"))
        elif data["destClient"] == "Voorraad":
            sock.connect(VoorraadIP, 9090)
            sock.sendall(bytes(data, encoding="utf-8"))
        elif data["destClient"] == "Productie":
            sock.connect(ProductieIP, 9090)
            sock.sendall(bytes(data, encoding="utf-8"))




        connection.sendall(str.encode("Idk"))
    connection.close()

#accepteert nieuwe verbindingen
while True:
    Client, address = ServerSideSocket.accept()
    print('Volgend IP adres is nu verbonden: ' + address[0] + ', address is: ' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()