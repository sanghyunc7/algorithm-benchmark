def combinations(n):
    letters = [c for c in str(n)]
    
    # 123 -> 213, 132, 321, 312, 231
    ans = set()
    used = set() # indices in use
    def helper(tmp):
        if len(used) == len(letters):
            ans.add(int("".join(tmp)))
            return
        
        for i in range(len(letters)):
            if i in used or letters[i] == '0' and len(tmp) == 0:
                continue
            used.add(i)
            tmp.append(letters[i])
            helper(tmp)
            tmp.pop()
            used.remove(i)
    
    helper([])
    return list(ans)

print(combinations(1111))