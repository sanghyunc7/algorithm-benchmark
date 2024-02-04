# dict is ordered. set is unordered.
d = {}
d[9] = 9
d[8] = 8
d[7] = 7
d[11] = 11
d[10] = 10
print(d)


s = set()
s.add(9)
s.add(8)
s.add(7)
s.add(13)
s.add(12)
s.add(11)
print(s)
# output
# {9: 9, 8: 8, 7: 7, 11: 11, 10: 10}
# {7, 8, 9, 11, 12, 13}
