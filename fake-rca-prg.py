def get_prg(plaintext_size, k):
    bak = bytearray(k, 'ascii') 
    prg = []
    i = j = 0
    for r in range(0, plaintext_size):
        i = (i + 1)%32
        j = (j + bak[i])%32
       
        bak[i], bak[j] = bak[j], bak[i]
        
        res = bak[(bak[i] + bak[j])%32] 
        
       # print(repr(res))
        
        prg.append(res) 
    return bytes(prg).decode("ascii")# return keystream

def fake_rc4(plaintext, keystream):
     p = bytes(plaintext, 'ascii')
     ks = bytes(keystream, 'ascii')
    
     return bytes(a ^ b for a, b in zip(p, ks)).decode("utf-8") 
