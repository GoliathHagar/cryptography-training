#
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
                [char_frequencies.get(chr(byte), default_frequencies) for byte in input_bytes.lower()]
            )
    )


def single_byte_xor(input_byte, character):
    output_byte = b''

    for byte in input_byte:
        output_byte += bytes([byte ^ character])

    return output_byte


def brute_force_xor(cypher_text):
    potential_message = []

    for possible_key in range(256):
        message = single_byte_xor(cypher_text, possible_key)
        score = english_score(message)
        data = {
            'message': message,
            'score': score,
            'possible_key': possible_key
        }
        potential_message.append(data)

    best_score = sorted(potential_message, key=lambda x: x['score'], reverse=True)

    return best_score[0]


def main():
    cyphertext = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

    item = brute_force_xor(cyphertext)

    print("key: ", item.get("possible_key"), "message: ", item.get("message").decode(), " score: ", item.get("score"))


if __name__ == "__main__":
    main()
