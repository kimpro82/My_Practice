# Each server/client side codes should be run by different kernel from each other.

# 3. UDP Server

from socket import * # import socket module

# declare variables of ip and port address
server_ip, server_port = "127.0.0.1", 12345

server_sock = socket(AF_INET, SOCK_DGRAM) # generate a socket instance
server_sock.bind((server_ip, server_port)) # bind ip and port address

server_sock.settimeout(10) # define timeout limit : "10" seconds

# recieve data from the client within '1024' byte
data, client_addr = server_sock.recvfrom(1024)

# print the client's IP address and recieved data
print("보낸 IP : ", client_addr)
print("받은 데이터 : ", data.decode())

server_sock.close() # close the server
