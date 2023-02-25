def d1(n):
    r = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)


# print(d1(117)) [1, 3, 9, 13, 39, 117]
# print(d1(119)) [1, 7, 17, 119]
# print(d1(121)) [1, 11, 121]

from re import fullmatch

a = []
for i in range(117, 10**8 + 1, 117):
    if fullmatch(r'1\d58\d*129', str(i)) and i % 119 != 0 and i % 121 != 0:
        a.append((i, i // 117))
for i in range(119, 10**8 + 1, 119):
    if fullmatch(r'1\d58\d*129', str(i)) and i % 117 != 0 and i % 121 != 0:
        a.append((i, i // 119))
for i in range(121, 10**8 + 1, 121):
    if fullmatch(r'1\d58\d*129', str(i)) and i % 119 != 0 and i % 117 != 0:
        a.append((i, i // 121))
print(*sorted(a), sep='\n')