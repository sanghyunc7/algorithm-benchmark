def solution(low, high):
    # each digit must be unique

    ans = []
    for i in range(low, high + 1):
        ans.append(i)
        sub = set()
        while i > 0:
            sub.add(i % 10)
            i = i // 10
        if len(sub) != 3:
            ans.pop()
    print(ans)
    return ans


def solution1(low, high):
    ans = []
    for i in range(low, high + 1):
        s = str(i)
        chars = set([c for c in s])
        if len(chars) == 3:
            ans.append(i)
    print(ans)
    return ans


print(solution(100, 200) == solution1(100, 200))