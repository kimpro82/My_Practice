# FTP - get the server's file list

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
