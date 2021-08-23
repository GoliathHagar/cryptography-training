# HEXADECIMAL TO BASE64 CRYPTOGRAPHY

import base64


def main():
    hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    rawhex = bytes.fromhex(hexstring)

    b64 = base64.b64encode(rawhex).decode()

    print("Base64 Encoded: ", b64)


if __name__ == "__main__":
    main()
