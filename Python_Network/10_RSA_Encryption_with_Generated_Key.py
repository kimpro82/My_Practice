# Simple Encryption : RSA with using generated key

# import packages related with RSA encryption
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA

# function of generating private key and public key
def create_PEM() :
    private_key = RSA.generate(1024) # generate private key
    h = open('private_key.pem', 'wb+')
    h.write(private_key.exportKey('PEM')) # write private key on file
    h.close()
    
    public_key = private_key.publickey() # generate public key
    h = open('public_key.pem', 'wb+')
    h.write(public_key.exportKey('PEM')) # write public key on file
    h.close()

create_PEM()

# function of reading key
def readPEM(pemfile) :
    h = open(pemfile, 'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

# function of RSA enctyption
def rsa_enc2(msg) :
    public_key = readPEM('public_key.pem') # read public key
    cipher = PKCS1_OAEP.new(public_key) # add padding to public key
    enc_data=cipher.encrypt(msg) # message encryption
    return enc_data

# function of RSA decryption
def rsa_dec2(msg) :
    private_key = readPEM('private_key.pem') # read private key
    cipher = PKCS1_OAEP.new(private_key) ## add padding to private key
    dec_data = cipher.decrypt(msg) # message decryption
    return dec_data

# do
if __name__ == '__main__' :
    msg = 'I love red flavor'
    cipher_text = rsa_enc2(msg.encode('utf-8'))
    print('cipher text : ', cipher_text)
    
    plain_text = rsa_dec2(cipher_text)
    print('plain text : ', plain_text)
