from Crypto.Cipher import AES
from Crypto import Random

def aes_encrypt(plaintext, k):
    iv = Random.new().read(16)
    cipher = AES.new(k, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(plaintext)    
    
    return iv+ct_bytes

def aes_decrypt(ciphertext, k):
    iv = ciphertext[:16]
    
    cipher = AES.new(k, AES.MODE_CBC, iv)
    pt = cipher.decrypt(ciphertext[16:])
    
    return str(pt, 'latin1')
