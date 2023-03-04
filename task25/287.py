def d1(n):
    r = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)


# for x in range(10):
#     for y in [''] + list(range(1000)):
#         for z in [''] + list(range(1000)):
#             s =f'{y}2{x}2{z}'
#             i = int(s)
#             if i < 10**7 and s == s[::-1] and i % 53 == 0 and len(d1(i)) > 30:
#                 print(i, sum(d1(i)))


from re import fullmatch

for x in range(53, 10**7, 53):
    s = str(x)
    if fullmatch(r'\d*2\d2\d*', str(x)) and s == s[::-1] and len(d1(x)) > 30:
        print(x, sum(d1(x)))