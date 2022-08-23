alphabet = "abcdefghijklmnopqrstuvwxyz"
def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def english_score(input_bytes):
    default_frequencies = 0 #Penality for nom english ascii "e" value
    char_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return (
            sum(
                [char_frequencies.get(chr(byte), default_frequencies) 
                for byte in input_bytes.lower()]
            )
    )
    
if __name__ == "__main__":
    brute_force = "kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe"
    scored = []
    
    for k in range(1, 25):
        dc = decrypt(brute_force, k)
        ddc = {"key": k, "message": dc, "score":english_score(bytes(dc, 'ascii')) }
        scored.append(
            ddc
        ) 
        
        #print(ddc)
    
    sorted_score = sorted( scored, key=lambda x: x['score'], reverse=True)
    
    print(sorted_score[0])
       

    
