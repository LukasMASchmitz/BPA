import random 

klanten = dict()
subOrders = dict()
Orders = list()


#slaat klanten op en geeft ze een klantnummer
def saveCustomer(naam):
    try:
        klanten[naam]
    except:
        klanten[naam] = len(klanten)+1


#slaat subOrders op per klant
def createSubOrders(klantnummer):
    subOrderCreated = False

    try:
        subOrders[klantnummer]
    except:
        subOrders[klantnummer] = [1]
        subOrderCreated = True
    
    if subOrderCreated == False:
        subOrders[klantnummer].append(len(subOrders[klantnummer])+1)


def CompileOrderDetails(ordernr, subordernr, klantnr, naam, bloktype, aantal, startperiode):
    Orders.append({"Ordernummer" : ordernr, "SubOrder" : subordernr , "Klantnummer" : klantnr, "naam" : naam, "Bloktype" : bloktype, "aantal" : aantal, "ontvangstpreiode" : startperiode})

def createOrder(naam, bloktype, aantal, periode):
    saveCustomer(naam)
    createSubOrders(klanten[naam])
    
    ordernr = len(Orders)+1
    klantnr = klanten[naam]
    subOrder = subOrders[klantnr][len(subOrders[klantnr])-1]

    CompileOrderDetails(ordernr, subOrder, klantnr, naam, bloktype, aantal, periode)










#-------------------TEST----------------------#

namen = ["Lukas", "Pepijn", "Dennis", "Jordy", "Chris"]
bloktypen = ["A", "B", "C"]
periode = 0
for i in range(20):
    naam = namen[random.randint(0, 4)]
    bloktype = bloktypen[random.randint(0, 2)]
    aantal = random.randint(1, 3)
    periode+=1

    createOrder(naam, bloktype, aantal, periode)


print(klanten)
print("______________________________________")
print(subOrders)
print("______________________________________")
for order in Orders:
    #print("ORDER ", order["ordernummer"])
    print (order)
print("______________________________________")