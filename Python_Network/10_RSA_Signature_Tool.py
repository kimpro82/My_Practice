# signature tool for RSA public key

# import packages related with RSA encryption
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA
import os

# function of reading key
def readPEM2(pemfile) :
    h = open(pemfile, 'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

# function of RSA sign
def rsa_sign(msg) :
    private_key = readPEM2('private_key.pem') # read private key
    public_key = private_key.publickey() # generate public key from private key
    h = SHA.new(msg) # hashing msg by SHA256
    sign = pkcs1_15.new(private_key).sign(h) # sign by private key
    return public_key, sign

# function of verification by piblic key
def rsa_verify(msg, public_key, sign) :
    h = SHA.new(msg)
    
    try :
        pkcs1_15.new(public_key).verify(h, sigh)
        print('인증합니다')
    except Exception as e :
        print(e)
        print('인증 못 합니다.')
# do
if __name__ == '__main__' :
    msg = 'I love strawberry'
    public_key, sign = rsa_sign(msg.encode('utf-8'))
    rsa_verify(msg.encode('utf-8'), public_key, sign)
