import socket

HOST ='127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((HOST,PORT))
    
    while True:
        msg_client=input("client:")
        client.sendall(msg_client.encoded())
        
        data=client.recv(1024)
        print(data.decode())