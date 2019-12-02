# Encryption & Decryption by Columnar Transformation Cipher


# Funtion of Generating Key Tables
def create_key_table(key) :
    enckey_table = {}
    deckey_table = {}
    
    for i, k in enumerate(key) :
        enckey_table[i] = int(k)-1
        deckey_table[int(k)-1] = i
        
    return enckey_table, deckey_table


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
