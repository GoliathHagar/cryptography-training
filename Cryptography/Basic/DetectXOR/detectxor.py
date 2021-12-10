from Cryptography.Basic.SingleByteXOR.singlebytexor import brute_force_xor


def file_brute_force_xor(ciphers):
    potential_plaintext = []

    for hexa in ciphers:
        ciphertext = bytes.fromhex(hexa)
        potential_plaintext.append(brute_force_xor(ciphertext))

    best_score = sorted(potential_plaintext, key=lambda x: x['score'], reverse=True)[0]

    return best_score


def main():
    ciphers = open('encrypted.txt').read().splitlines()

    item = file_brute_force_xor(ciphers)

    print("key: ", item.get("possible_key"), "message: ", item.get("message").decode(), " score: ", item.get("score"))


if __name__ == "__main__":
    main()
