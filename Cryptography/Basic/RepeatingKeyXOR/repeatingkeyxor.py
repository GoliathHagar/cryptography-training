import base64
import math
from Cryptography.Basic.SingleByteXOR.singlebytexor import brute_force_xor, english_score


def repeating_key_xor(message_bytes, key):
    output_bytes = b''
    index = 0

    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1

    return output_bytes


def hamming_distance(text1: bytes, text2: bytes) -> int:
    BYTE_ONE: str = "1"
    dist: int = 0

    for byte1, byte2 in zip(text1, text2):
        dist += bin(byte1 ^ byte2).count(BYTE_ONE)

    return dist


def hamming_score_bytes(byte1: bytes, byte2: bytes) -> float:
    NUMBER_OF_BITS: int = 8

    return hamming_distance(byte1, byte2) / (NUMBER_OF_BITS * min(len(byte1), len(byte2)))


def compute_key_size(text: bytes) -> list[dict]:
    possible_key_sizes = []

    for key_size in range(2, math.ceil(len(text) / 3)):
        chunks = [text[i: i + key_size] for i in range(0, len(text), key_size)]

        if len(chunks) >= 2 and len(chunks[-1]) <= len(chunks[-2]) / 2:
            chunks.pop()

        _scores = []

        for i in range(0, len(chunks) - 1, 1):
            for j in range(i + 1, len(chunks), 1):
                _scores.append(hamming_score_bytes(chunks[i], chunks[j]))

        score = sum(_scores) / len(_scores)

        possible_key_sizes.append(
            {
                'key_size': key_size,
                'score': score
            }
        )

    possible_key_sizes = sorted(possible_key_sizes, key=lambda x: x['score'])

    return possible_key_sizes


def breaking_repeating_key_xor(ciphertext: bytes, top_score=20):  # best top 20 score key size
    possible_key_sizes = compute_key_size(ciphertext)
    top_sizes = top_score if len(possible_key_sizes) >= top_score else len(possible_key_sizes)

    possible_plaintext = []

    for top_size in range(top_sizes):  # top 3 key sizes
        possible_key_size = possible_key_sizes[top_size]  # best score key size

        key_size = possible_key_size['key_size']
        pkey = b''

        for i in range(key_size):
            block = b''

            for j in range(i, len(ciphertext), key_size):  # create a singleByte ciphertext(block) at key positions
                block += bytes([ciphertext[j]])

            pkey += bytes([brute_force_xor(block)['possible_key']])

        possible_plaintext.append(
            {
                'possible_message': repeating_key_xor(ciphertext, pkey),
                'possible_key': pkey
            }
        )

    max_english_scored = sorted(
        possible_plaintext,
        key=lambda x: english_score(x['possible_message'])
    )

    return max_english_scored[0]


def main():
    """
    :problems scores precisions(hamming and english), try top_score
    :return: None
    """
    ciphertext = b''
    message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICED"

    ciphertext = repeating_key_xor(message, key)

    print("repeatingkeyxored: ", ciphertext.hex())

    breaked = breaking_repeating_key_xor(ciphertext, 8)
    print("Key=", breaked['possible_key'].decode(), "\nbreaking=", breaked['possible_message'].decode())

    # with open('encripted.txt') as input_file:
    #     ciphertext = base64.b64decode(input_file.read())
    #
    # breaked = breaking_repeating_key_xor(ciphertext)
    # print("Key=", breaked['possible_key'].decode(), "\nbreaking=", breaked['possible_message'].decode())


if __name__ == "__main__":
    main()
