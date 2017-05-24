import threading
from socket import *
from consumers import pizza_done

def udpReceiveDataFor():
    HOST = ''
    PORT = 10053
    #PORT = 7788
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    sk = socket(AF_INET, SOCK_DGRAM)
    sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sk.bind(ADDR)

    while True:
        #print('waiting for message...')
        data, addr = sk.recvfrom(BUFSIZ)
        pizza_done.send(sender=addr,toppings=data,size=1024)
        #print(data)

t = threading.Thread(target=udpReceiveDataFor)
t.start()