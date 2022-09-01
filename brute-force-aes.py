from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english

def brute_force_aes(ciphertext):
    for x in range(1,999999):
        
        phone = '036' + str(x).zfill(6) + '0000000'
        d = aes_decrypt(ciphertext, bytes(phone, 'ascii'))
        
        
        if is_english(d):
            return d, phone.encode() #I don't like two returns but for now...
            
    return "test:", "Failed"# return plaintext (in 'latin1', from aes_decrypt()), k
