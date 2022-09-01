from collections import Counter

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
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

    score  = (
            sum(
                [char_frequencies.get(chr(byte), default_frequencies) 
                for byte in bytes(s.lower(), 'ascii')]
            )
    )
    
    if score > 0.5:
        return True
        
    return False # return boolean
