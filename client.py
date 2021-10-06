import time
import socket
import random

for i in range(10):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    ranNum = random.randint(0,25)
    msg = s.recv(ranNum)
    print(msg.decode("utf-8"))
    time.sleep(3)

'''import socket
##comment
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))
'''