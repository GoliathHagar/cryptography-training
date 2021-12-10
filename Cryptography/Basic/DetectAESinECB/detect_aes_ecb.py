def detect_aes_ecb(cyphers):
    aes_ecb_cypher: dict(str, int, int) = []

    for cypher in cyphers:
        blocks = break_in_block16(cypher)
        blocks_set = set(blocks)

        if len(blocks) != len(blocks_set):
            aes_ecb_cypher.append(
                {
                    "cypher_text": cypher,
                    "blocks": len(blocks) - len(blocks_set) + 1,
                    "line": cyphers.index(cypher) + 1
                }
            )

    return aes_ecb_cypher


def break_in_block16(cypher):
    chunk_size = 16
    return [cypher[i: i + chunk_size] for i in range(0, len(cypher), chunk_size)]


def main():
    cyphers = open('cyphers.txt').read().splitlines()

    for ecb in detect_aes_ecb(cyphers):
        print(
            f"Duplicate Blocks = {ecb.get('blocks')}\nFile line = {ecb.get('line')}\nCypherText = {ecb.get('cypher_text')}")
    pass


if __name__ == '__main__':
    main()
