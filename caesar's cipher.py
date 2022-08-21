alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    cipherText = ''

    for caracter in plaintext:
        position = alphabet.find(caracter)
        
        #debug
        #prt = {'position':position, 'caracter':caracter}
        #print(prt)
        if position == -1: #add space and caracters not in alphabet (may cause problems when decrypting...)
            cipherText += caracter
            continue
    
        cipherText += alphabet[position-k]
        
    #print(cipherText)
    
    return cipherText # do stuff and return ciphertext
