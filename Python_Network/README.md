# My Python Practice - Network & Security
- TCP_Server.py (2019.10.13)
- TCP_Client.py (2019.10.13)
- UDP_Server.py (2019.10.13)
- UDP_Client.py (2019.10.13)


## TCP/UDP Server-Client Programming Basic Practice (2019.10.13)
 
![TCPUDP](https://github.com/kimpro82/My_Practice/blob/master/images/범죄와의전쟁_최민식_느그서장이랑.jpg)  
내가 인마! 서버랑 클라이언트랑 마! 소켓 열고! 메세지 보내고! TCP랑 UDP랑 다 했어!
  
※ Each server/client side codes should be run by different kernel from each other. 

### TCP_Server.py (2019.10.13)

```python
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
```
> ('127.0.0.1', 54476) 에서 접속이 확인되었습니다.  
> 받는 데이터 : 저는 클라이언트입니다.  
> 메세지를 보냈습니다.  

### TCP_Client.py (2019.10.13)

```python
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
```
> 연결이 확인되었습니다.  
> 메세지를 전송했습니다.  
> 받는 데이터 : 저는 서버입니다.  

### UDP_Server.py (2019.10.13)

```python
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
```
> 보낸 IP :  ('127.0.0.1', 64201)  
> 받은 데이터 :  Hi! Server.  

### UDP_Client.py (2019.10.13)

```python
from socket import * # import socket module

# declare variables of ip and port address
server_ip, server_port = "127.0.0.1", 12345

# generate a socket instance
client_sock = socket(AF_INET, SOCK_DGRAM) 

# send data to the server
client_sock.sendto("Hi! Server.".encode(),(server_ip, server_port))

client_sock.close() # close the client's socket
```
