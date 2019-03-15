import time
from scapy.layers.l2 import arping
print("Import succesfull")
def parsePacket(resp,hostList):
    for item in resp[0]:
        inHost = True
        for host in hostList:
            if item[1].psrc in host:
                inHost = True
                break
            else:
                inHost = False
        if inHost == False:
            hostList.append(dict({item[1].psrc: item[1].hwsrc}))
            print("Captured IP and MAC -->",dict({item[1].psrc: item[1].hwsrc}) )
            print("[*]Discovered hosts: ",hostNumber)

if __name__ == "__main__":
    #resp[0]             ---> arping results
    #resp[0][0]          ---> first packet
    #resp[0][0][1].hwsrc ---> captured packets, hwsrc
    hostList = []
    ipRange = input("Enter ip range :")
    resp = arping(ipRange,verbose=False)
    hostNumber = len(resp[0])
    print("[*]Given range:" + str(ipRange))
    # initial parsing
    for item in resp[0]:
        hostList.append(dict({item[1].psrc: item[1].hwsrc}))
    for item in hostList:
        print("Captured IP and MAC -->", item)
    print("[*]Discovered hosts: ",hostNumber)

    while(True):
        print("[*]Continuing to discovery ")
        resp = arping(ipRange, verbose=False)
        parsePacket(resp,hostList)
        time.sleep(5)
