import time
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    previewTime = 0.1 # initial waiting time...
    possiblePassword = list('0000')
    matchFound = ''

    for digit in range(4):#4 didit password
        for possibleDigit in range(0,10):#generate digits
        
            possiblePassword[digit] = str(possibleDigit)
            
            startTime = time.time()
            found = check_password(possiblePassword)
            endTime = time.time()
            
            elaspseTime = float("{:.2f}".format(endTime - startTime))
            
            pwd = "".join(possiblePassword)
            
            #debug only
            #prt = {'digit': digit, 'possibleDigit': possibleDigit, 'pwd': pwd, 'elaspseTime': elaspseTime, 'previewTime': previewTime}
            #print(prt)
            
            if found:
                matchFound = pwd;
            
            if elaspseTime > previewTime:
                previewTime = elaspseTime
                break
            
        
    return matchFound # return cracked password

