import socket

host="192.168.1.11"
port=1234

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((host,port))
    userinput=str(input())
    s.sendto(userinput.encode(),(host,port))
    msg,addr = s.recvfrom(1024) 
    print('Received:' + msg.decode())
    while userinput!="bye": #recieve messeges on loop
        userinput=str(input())
        s.sendto(userinput.encode(),(host,port))
        msg,addr = s.recvfrom(1024)
        print('Received:' + msg.decode())
        
    s.close()
