c1 = bytes.fromhex('561034f8')
c2 = bytes.fromhex('46063ef3')

ball= bytes.fromhex('34715894')
cake = bytes.fromhex('35715f9d')
poem = bytes.fromhex('267f5195')

ms = [ball, cake, poem]

print(c1)
print(c2)
print(ball)
print(cake)
print(poem)

k = []

for m in ms:
    c = bytes([mm ^ cc for mm, cc in zip(m, c2)])
    k += c
    print(c)
print(k)
