
from Cryptography.Basic.SingleByteXOR.singlebytexor import brute_force_xor


def file_brute_force_xor(ciphers):
    potencial_plaintext = []
    
    for hex in ciphers:
        ciphertext = bytes.fromhex(hex)
        potencial_plaintext.append(brute_force_xor(ciphertext))

    best_score = sorted(potencial_plaintext, key= lambda x: x['score'], reverse=True)[0]

    return best_score

def main():
    ciphers = open('encripted.txt').read().splitlines()

    item = file_brute_force_xor(ciphers)

    print("key: ", item.get("possible_key"), "message: ", item.get("message").decode(), " score: ", item.get("score"))


if __name__ == "__main__":
    main()
