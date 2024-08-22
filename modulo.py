base = 26
mod = 415

# create prefix sum array for hashes
# does hash("345") created from scratch have the same value as prefix[-2] - prefix[2]?

powers = [1]
for i in range(1, 20):
    powers.append((powers[-1] * base) % mod)
print(powers)

hash_scratch = 0
n = "345"
for i in range(len(n)):
    c = int(n[i])
    hash_scratch = (c * powers[i] + hash_scratch) % mod
print("scratch", hash_scratch)


prefix = [0]
n = "123456"
for i in range(len(n)):
    c = int(n[i])
    prefix.append((c * powers[i] + prefix[-1]) % mod)

print(prefix)

hash_prefix = ((prefix[-2] - prefix[2]) / powers[2]) % mod
print(hash_prefix)












