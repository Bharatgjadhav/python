import socket

HOST ='127.0.0.1'
PORT=8081

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    conn, addr = server.accept()
    print('connect with client:{}'.format(addr))
    
    with conn:
        while True:
            msg_client=conn.recv(1024)
            print(msg_client.decode()) 
            
            msg_server=input('server:')
            conn.sendall(msg_server.encoded())