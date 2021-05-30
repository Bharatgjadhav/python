import socket

HOST ='127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    conn, addr = server.accept()
    print('connect with client:{}'.format(addr))
    
    with conn:
        while True:
            data=conn.recv(1024)
            print(data.decode()) 
            
            msg_server=input('server:')
            conn.sendall(msg_server.encoded())
            
            
             
     
    
    