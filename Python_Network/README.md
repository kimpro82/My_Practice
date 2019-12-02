# My Python Practice - Network & Security

![TCPUDP](https://github.com/kimpro82/My_Practice/blob/master/images/범죄와의전쟁_최민식_느그서장이랑.jpg)  
"내가 인마! 서버랑 클라이언트랑 마! 소켓 열고! 메세지 보내고! TCP랑 UDP랑 다 했어!"

- 8_Columnar_Transformation_Cipher.py (2019.11.24)
- 7_Basic_Encryption.py (2019.11.24)
- 5_FTP_1.py (2019.10.27)
- 5_FTP_2.py (2019.10.27)
- 2_TCP_Echo_Server.py (2019.10.20)
- 2_TCP_Echo_Client.py (2019.10.20)
- 2_UDP_Echo_Server.py (2019.10.20)
- 2_UDP_Echo_Client.py (2019.10.20)
- 1_TCP_Server.py (2019.10.13)
- 1_TCP_Client.py (2019.10.13)
- 1_UDP_Server.py (2019.10.13)
- 1_UDP_Client.py (2019.10.13)

※ Each server/client side codes should be run by different kernel from each other. 

## 8. Encryption & Decryption by Columnar Transformation Cipher (2019.11.24)

### 8_Columnar_Transformation_Cipher.py (2019.11.24)
make functions of generating key tables, plain text(add padding), encryption and decryption
```python
# Funtion of Generating Key Tables
def create_key_table(key) :
    enckey_table = {}
    deckey_table = {}
    
    for i, k in enumerate(key) :
        enckey_table[i] = int(k)-1
        deckey_table[int(k)-1] = i
        
    return enckey_table, deckey_table
```

```python
# Function of Generating Plain Text
def create_plain_text(msg, key) :
    msglen = len(msg)
    keylen = len(key)
    
    if (msglen % keylen) != 0 :
        j = keylen - (msglen % keylen)
        for i in range(0, j) :
            msg = msg + '0'
    
    return msg
    key_len = len(key_table)
    cipher_text = ''
    buf = ['']*key_len
    
    for i, c in enumerate(plain_text) :
        col = i % key_len
        index = key_table[col]
        buf[index] += c
        
    for txt in buf :
        cipher_text += txt
        
    return cipher_text
```

```python
# Function of Encryption
def encrypt(plain_text, key_table) :
    key_len = len(key_table)
    cipher_text = ''
    buf = ['']*key_len
    
    for i, c in enumerate(plain_text) :
        col = i % key_len
        index = key_table[col]
        buf[index] += c
    
    for txt in buf :
        cipher_text += txt
    
    return cipher_text
```

```python
# Function of Decryption
def decrypt(cipher_text, key_table) :
    msg_len = len(cipher_text)
    key_len = len(key_table)
    blocksize = int(msg_len / key_len)
    buf = ['']*key_len
    plain_text = ''
    
    for i in range(key_len) :
        index = key_table[i]
        buf[index] = cipher_text[i*blocksize : i*blocksize+blocksize]
    
    for i in range(blocksize) :
        for j in range(key_len) :
            if buf[j][i] != '0' :
                plain_text += buf[j][i]
    
    return plain_text
```

```python
# Do
if __name__ == '__main__' :
    msg = 'abcdef'
    print("Original Meassage : ", msg)
    
    key = '2413'
    print("Key : ", key)
    
    enckey_table, deckey_table = create_key_table(key)
    plain_text = create_plain_text(msg, key)
    
    cipher_text = encrypt(plain_text, enckey_table)
    
    print("Encrypted Message : ", cipher_text)
    
    plain_text2 = decrypt(cipher_text, deckey_table)
    print("Decrypted Message : ", plain_text2)
```

> Original Meassage :  abcdef  
> Key :  2413  
> Encrypted Message :  c0aed0bf  
> Decrypted Message :  abcdef  

## 7. Basic Encryption & Decryption (2019.11.24)

### 7_Basic_Encryption.py (2019.11.24)
make functions for generating codebook, encryption and decryption

```python
# Function of Generating Encryption Codebook
def createCodebook() :
    key = []
    value = []
    
    for i in list(range(97, 123)) :
        key.append(chr(i))
        value.append(chr(i-64))

    encbook = dict(zip(key, value))
    decbook = dict(zip(value, key))

    return encbook, decbook    
```
```python
# Function of Encryption
def encrypt(msg, encbook) :
    for c in msg :
        if c in encbook :
            msg = msg.replace(c, encbook[c])
    
    return msg
```
```python
# Function of Decryption
def decrypt(msg, encbook) :
    for c in msg :
        if c in decbook :
            msg = msg.replace(c, decbook[c])
    
    return msg
```

practice
```python
if __name__ == '__main__' :
    plain_text = 'live for your smile and die for your kiss'
    print("Original Message : ", plain_text)
    
    encbook, decbook = createCodebook()
    cipher_text = encrypt(plain_text, encbook)
    print("Encrypted Message : ", cipher_text)
    
    decipher_text = decrypt(cipher_text, decbook)
    print("Decrypted Message : ", decipher_text)
```
> Original Message :  live for your smile and die for your kiss  
> Encrypted Message :  ,)6% &/2 9/52 3-),% !.$ $)% &/2 9/52 +)33  
> Decrypted Message :  live for your smile and die for your kiss

## 6. E-mail Program

## 5. FTP Client Programming (2019.10.27)

### 5_FTP_1.py (2019.10.27)
get the server's file list
```python
import ftplib # import a module about ftp

# declare parameters for ftplib.FTP()
FTP_SERVER_URL = "ftp.gnu.org"
username = "anonymous"
email = ""

# generate FTP clent's session
ftp = ftplib.FTP(FTP_SERVER_URL, username, email)

ftp.cwd("/pub") # change FTP directory
print("사이트 : ", FTP_SERVER_URL, "의 파일목록")
ftp.dir() # get the list of the server's directories
```
![ftp.dir()](https://github.com/kimpro82/My_Practice/blob/master/images/2019-10-27%2020%3B29%3B39%20HW3-1%20Result.PNG)  

### 5_FTP_2.py (2019.10.27)
file upload to the FTP server
```python
import ftplib
import os

# declare parameters
FTP_SERVER = "localhost"
FILE_NAME = "sample.txt"
username = ""
password = ""

print(FTP_SERVER, "FTP 서버에 접속합니다.")
ftp = ftplib.FTP(FTP_SERVER) # connectthe FTP server
print(username, "가 서버에 로그인합니다.")
ftp.login(username, password) # login the server

os.chdir("c:\\ftp_test2")
myfile = open(FILE_NAME, 'rb')

ftp.storbinary("STOR sample.txt", myfile) # upload a binary file to the server

print(FILE_NAME, "파일을 업로드 하였습니다.")
myfile.close() # finish file uploading

ftp.quit() # finish the connection with the server
```
> localhost FTP 서버에 접속합니다.  
> test 가 서버에 로그인합니다.  
> sample.txt 파일을 업로드 하였습니다.  
> Out[3]: '221 Goodbye'  

## 4. Advanced Chating Program with Threading

## 3. Chating Program

## 2. TCP/UDP Server-Client Programming 2 - Reflect Echo (2019.10.20)

### TCP_Echo_Server.py (2019.10.20)

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

data = "none"

while len(data) : # infinite loop (len(data)>0 : True)
    data = connectionSock.recv(1024) # receive data
    print("받은 데이터 :", data.decode('utf-8'))
    connectionSock.send(data) # send data
    print("송신 데이터 :", data.decode('utf-8'), "메세지를 보냈습니다.")

connectionSock.close() # close the connection
server_sock.close() # close the server

```
> ('127.0.0.1', 53013) 에서 접속이 확인되었습니다.  
> 받은 데이터 : 안녕하세요  
> 송신 데이터 : 안녕하세요 메세지를 보냈습니다.  
> 받은 데이터 : 저는 임꺽정이라고 합니다  
> 송신 데이터 : 저는 임꺽정이라고 합니다 메세지를 보냈습니다.  


### TCP_Echo_Client.py (2019.10.20)

```python
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
```

> 데이터 입력 :안녕하세요  
> 받은 데이터 : 안녕하세요  
>  
> 데이터 입력 :저는 임꺽정이라고 합니다  
> 받은 데이터 : 저는 임꺽정이라고 합니다  


### UDP_Echo_Server.py (2019.10.20)

```python
from socket import * # import socket module

# declare variables of ip and port address
server_ip, server_port = "127.0.0.1", 12345

server_sock = socket(AF_INET, SOCK_DGRAM) # generate a socket instance
server_sock.bind((server_ip, server_port)) # bind ip and port address

# recieve data from the client within '1024' byte
data, client_addr = server_sock.recvfrom(1024)

while data != "끝" : # program ending message : "끝"
    # print the client's IP address and recieved data
    print("보낸 IP : ", client_addr)
    print("받은 데이터 : ", data.decode())
    print()
    server_sock.sendto(data, client_addr) # send data
    data, client_addr = server_sock.recvfrom(2024) # receive data

server_sock.close() # close the server
```

> 보낸 IP :  ('127.0.0.1', 50561)  
> 받은 데이터 :  안녕하세요  
>  
> 보낸 IP :  ('127.0.0.1', 50561)  
> 받은 데이터 :  저는 임꺽정입니다  
>  
> 보낸 IP :  ('127.0.0.1', 50561)  
> 받은 데이터 :  끝  


### UDP_Echo_Client.py (2019.10.20)

```python
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
```

> 데이터 입력 :안녕하세요  
> Echo data : 안녕하세요  
>  
> 데이터 입력 :저는 임꺽정입니다  
> Echo data : 저는 임꺽정입니다  
>  
> 데이터 입력 :끝  


## 1. TCP/UDP Server-Client Programming 1 - Basic Practice (2019.10.13)

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
