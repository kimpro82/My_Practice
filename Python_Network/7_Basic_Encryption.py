# Basic Encryption & Decryption

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


# Function of Encryption
def encrypt(msg, encbook) :
    for c in msg :
        if c in encbook :
            msg = msg.replace(c, encbook[c])
    
    return msg

# Function of Decryption
def decrypt(msg, encbook) :
    for c in msg :
        if c in decbook :
            msg = msg.replace(c, decbook[c])
    
    return msg

# Do
if __name__ == '__main__' :
    plain_text = 'live for your smile and die for your kiss'
    print("Original Message : ", plain_text)
    
    encbook, decbook = createCodebook()
    cipher_text = encrypt(plain_text, encbook)
    print("Encrypted Message : ", cipher_text)
    
    decipher_text = decrypt(cipher_text, decbook)
    print("Decrypted Message : ", decipher_text)
