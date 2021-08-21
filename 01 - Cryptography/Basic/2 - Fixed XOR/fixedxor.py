
def sxor(s1,s2):
    return bytes([_a ^ _b for _a, _b in zip(s1,s2)])

def main():
    byte1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    byte2 = bytes.fromhex("686974207468652062756c6c277320657965")

    hexdec = sxor(byte1, byte2)

    print("hexadecimal decoded: ", hexdec.hex())


if __name__ == "__main__":
    main()
