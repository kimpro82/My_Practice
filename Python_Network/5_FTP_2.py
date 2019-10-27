# FTP - file upload

# import required modules
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
