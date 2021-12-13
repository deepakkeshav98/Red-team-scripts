import socket
import sys

port=int(sys.argv[1])

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind(('',port))
    message, addr = s.recvfrom(1024)
    print("CONNECTION FROM:", str(addr))
    print('Received:' + message.decode())
    userinput=str(input())
    s.sendto(userinput.encode(),addr)
    while userinput!="bye":
        msg,addr = s.recvfrom(1024)
        print('Received:' + msg.decode())
        userinput=str(input())
        s.sendto(userinput.encode(),addr)
        
    s.close()
