import base64

from Cryptodome.Cipher import AES


def decrypt_aes_ebc(key, cyphers):
    potential_plaintext = []

    dec = AES.new(key=key, mode=AES.MODE_ECB)

    cyphertext = base64.b64decode(cyphers)

    potential_plaintext.append(dec.decrypt(cyphertext))

    return potential_plaintext


def main():
    key = b'YELLOW SUBMARINE'

    cyphers = open('encrypted.txt').read().replace('\n', '')

    for dc in decrypt_aes_ebc(key=key, cyphers=cyphers):
        print(dc)


if __name__ == '__main__':
    main()
