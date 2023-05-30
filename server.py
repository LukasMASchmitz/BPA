import socket
import os
from _thread import *
import json

ServerSideSocket = socket.socket()
host = '192.168.100.57'
port = 9090
ThreadCount = 0

global KlantIp
global PlanningIP
global AccountmanagerIP

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

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

        #volgende elifs zijn om data naar destination te sturen
        #if data[1] == "Accountmanager":

        #elif data[1] == "Planning":






        connection.sendall(str.encode("Het werkt"))
    connection.close()


while True:
    Client, address = ServerSideSocket.accept()
    print('Volgend IP adres is nu verbonden: ' + address[0] + ', address is: ' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()