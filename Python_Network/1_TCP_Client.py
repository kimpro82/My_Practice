# Each server/client side codes should be run by different kernel from each other.

# 2. TCP Client

from socket import * # import socket module

# declare variables of ip and port address
server_ip, server_port = "127.0.0.1", 12345

client_sock = socket(AF_INET, SOCK_STREAM) # generate a socket instance

# connect to the server with binding ip and port address
client_sock.connect((server_ip, server_port))
print("연결이 확인되었습니다.")

# send data to the server
client_sock.send("저는 클라이언트입니다.".encode('utf-8'))
print("메세지를 전송했습니다.")

# recieve data from the server
data = client_sock.recv(1024)
print("받는 데이터 :", data.decode('utf-8'))

client_sock.close() # close the client's socket
