import socket

HOST ='127.0.0.1'
PORT=8081

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((HOST,PORT))
    
    while True:
        msg_client=input("client:")
        client.sendall(msg_client.encoded())

        msg_client=client.recv(1024)
        print(msg_client.decode())