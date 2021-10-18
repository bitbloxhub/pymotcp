import bson

__version__ = '0.1.0'

def read(sock):
    lendat = b""

    for _ in range(4):
        lendattmp += sock.recv(1)
        if lendattmp: lendat += lendattmp
    
    length = int.from_bytes(lendat, "big")

    docdat = b""

    for _ in range(length):
        docdattmp += sock.recv(1)
        if docdattmp: docdat += docdattmp

    return bson.loads(docdat)

def send(sock, doc):
    docbson = bson.dumps(doc)
    length = len(docbson).to_bytes(4, "big")
    sock.send(length)
    sock.send(docbson)