# Simple Encryption : RSA

# import packages related with RSA encryption
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# function of RSA encryption
def rsa_enc(msg) :
    private_key = RSA.generate(1024)
        # 1024 : must be a multiple of 256 and >=1024
    public_key = private_key.publickey() # call public key from private key
    cipher = PKCS1_OAEP.new(public_key) # add padding to public key
    enc_data=cipher.encrypt(msg) # message encryption
    print('cipher text : ', enc_data)
    
    cipher = PKCS1_OAEP.new(private_key) ## add padding to private key
    dec_data = cipher.decrypt(enc_data) # message decryption
    print('plain_text : ', dec_data)

# do
msg = 'I love you'
rsa_enc(msg.encode('utf-8'))
