import socket

host="192.168.1.11" #server ip
port=1234 #server port

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as w:
    w.connect((host,port)) #use connect() on client and bind() on server
    msg=""
    while msg!="bye": #recieve messeges on loop
        inputmsg=input()
        w.send(inputmsg.encode())
        msg = w.recv(1024)
        print('Received:' + msg.decode())
        
    w.close
