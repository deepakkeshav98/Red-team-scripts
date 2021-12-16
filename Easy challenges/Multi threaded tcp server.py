import socket
import sys
import threading
port=int(sys.argv[1])


class ClientThread(threading.Thread): 
 
    def __init__(self,ip,port): 
        threading.Thread.__init__(self) 
        self.ip = ip 
        self.port = port  
 
    def run(self): 
        userinput=""
        while userinput!="bye":
            msg = c.recv(1024)
            print('Received:' + msg.decode())
            userinput=str(input())
            c.send(userinput.encode())
        c.close()


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',port))

threads=[]
while True:
    s.listen()
    print("server listening ------")
    c, addr = s.accept()
    print("CONNECTION FROM:", str(addr))
    ip,Rport=addr
    newthread=ClientThread(ip,Rport)
    newthread.start() 
    threads.append(newthread)
    
for t in threads:
    t.join()
        
            
       