import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))



'''import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## AF_INET is just asking for an IPV4 Value, SOCK Stream is asking 
## a stream socket
s.bind((socket.gethostname(), 1234))
## .bind function is IP address and a port number to a 
# socket instance.
s.listen(5)# calling listen() makes a 
#           socket ready for accepting connections.
print("About to enter loop")
while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} address has been established")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
'''