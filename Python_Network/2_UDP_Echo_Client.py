#4. UDP Echo - Client

from socket import * # import socket module

# declare variables of ip and port address
server_ip, server_port = "127.0.0.1", 12345

# generate a socket instance
client_sock = socket(AF_INET, SOCK_DGRAM) 

# send data to the server
inputData = input("데이터 입력 :")
client_sock.sendto(inputData.encode(), (server_ip, server_port))

while inputData != "끝" : # program ending message : "끝"
    data, cliet_addr = client_sock.recvfrom(1024) # receive data
    print("Echo data :", data.decode())
    inputData = input("데이터 입력 :") # send data
    client_sock.sendto(inputData.encode(), (server_ip, server_port))

client_sock.close() # close the client's socket
