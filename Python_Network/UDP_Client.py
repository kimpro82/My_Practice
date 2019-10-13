# Each server/client side codes should be run by different kernel from each other.

# 4. UDP Client

from socket import * # import socket module

# declare variables of ip and port address
server_ip, server_port = "127.0.0.1", 12345

# generate a socket instance
client_sock = socket(AF_INET, SOCK_DGRAM) 

# send data to the server
client_sock.sendto("Hi! Server.".encode(),(server_ip, server_port))

client_sock.close() # close the client's socket
