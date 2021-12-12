import socket
import sys

port=int(sys.argv[1])

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(('',port))
    s.listen()
    c, addr = s.accept()
    print("CONNECTION FROM:", str(addr))
    userinput=str(input())
    c.send(userinput.encode())
    while userinput!="bye":
        msg = c.recv(1024)
        print('Received:' + msg.decode())
        userinput=str(input())
        c.send(userinput.encode())
        
    s.close()
