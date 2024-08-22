w = "abc"
base = 26
mod = 10 ** 9 + 7
place = 1
right = [w[::-1]]
hash
for i in range(len(w) -1, -1, -1):
    c = ord(w[i]) - ord('a')
    hash1 = (hash1 * base + c) % mod
    hash2 = (c * place + hash2) % mod
    if hash1 == hash2:
        if w == 'abc':
            print(w, i, w[:i], hash1, hash2)
        right.append(w[:i])
    place = (place * base) % mod

print()
print(right)