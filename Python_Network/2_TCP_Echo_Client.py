#2. TCP Echo - Client

from socket import * # import socket module

# declare variables of ip and port address
server_ip, server_port = "127.0.0.1", 12345

client_sock = socket(AF_INET, SOCK_STREAM) # generate a socket instance
# connect to the server with binding ip and port address
client_sock.connect((server_ip, server_port))

while True :
    inputData = input("데이터 입력 :")
    # send data to the server
    client_sock.send(inputData.encode('utf-8'))
    # recieve data from the server
    data = client_sock.recv(1024)
    print("받은 데이터 :", data.decode('utf-8'))

client_sock.close() # close the client's socket
