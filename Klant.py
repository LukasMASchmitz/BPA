import socket
import sys
import json

#zet hier het ip adres van de server
HOST, PORT = '192.168.1.140' , 9090

running = True

while running:

    naam = ''
    periode = 0
    ingevuld = False

    while naam == '':
        naam = input("naam: ")
    
    while not ingevuld:
        blockType = input("blocktype, kies er 1. (A/B/C): ")
        if blockType != "":
            blockType = blockType.upper()
            if blockType == 'A' or blockType == 'B' or blockType == 'C':
                ingevuld = True
            else:
                print("er ging iets fout, probeer het opnieuw.")

    ingevuld = False

    while not ingevuld:
        aantal = input("aantal: ")
        if aantal.isdigit():
            aantal = int(aantal)
            if aantal<1:
                print("Je moet minstens 1 artikel bestellen.")
            elif aantal>3:
                print("Je mag per bestelling maximaal 3 artikelen bestellen.")
            else:
                ingevuld = True
    
    while periode < 1:
        periode = input("periode: ")
        if periode.isdigit():
            periode = int(periode)

    klantorder = {"client": "Klant" , "destClient": "Accountmanager" , "MijnIP": HOST , "name": naam , "blockType": blockType , "aantal": aantal , "periode": periode}

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
