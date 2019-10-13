# Each server/client side codes should be run different kernel from each other.

# 1. TCP Server

from socket import * # import socket module

# declare variables of ip and port address
server_ip, server_port = "127.0.0.1", 12345

server_sock = socket(AF_INET, SOCK_STREAM) # generate a socket instance
server_sock.bind((server_ip, server_port)) # bind ip and port address
server_sock.listen(1) # open the port to "one" client

# wait connection from the client
connectionSock, client_addr = server_sock.accept()
print(str(client_addr), "에서 접속이 확인되었습니다.")

# recieve data from the client within '1024' byte
data = connectionSock.recv(1024)
print("받는 데이터 :", data.decode('utf-8'))

# send data to the client
connectionSock.send("저는 서버입니다.".encode('utf-8'))
print("메세지를 보냈습니다.")

connectionSock.close() # close the connection
server_sock.close() # close the server
