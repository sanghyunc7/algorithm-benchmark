def harness(a, b, c):
    print(a + b + c)


test = [1, 2, 8]
harness(*test)



def harness1(a, b, c):
    a[0] = 7
    print(sum(a) + b + c)


test = [[3, 0, 8], 2, 8]
harness1(*test)
print(test)