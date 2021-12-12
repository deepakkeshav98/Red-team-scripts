import socket

host="192.168.1.11"
port=1234

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((host,port))

    msg = s.recvfrom(1024) 
    while msg: #recieve messeges on loop
        print('Received:' + msg)
        msg = s.recvfrom(1024)
    s.close()
