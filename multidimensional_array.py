s = "123456789"
ans = [[0] * (len(s) + 1) for _ in range(2)]
print(ans)

ans[0][0] = 1
print(ans)
print()

ans = [[0] * (len(s) + 1)] * 2
ans[0][0] = 1
print(ans)
print()

ans = [[[] for _ in range(len(s) + 1)] for _ in range(2)]
print(ans)
ans[0][0].append(1)
print(ans)
