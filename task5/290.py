def alg(n):
    s1 = sum(map(int, str(n)))
    s2 = f'{s1:b}'
    if s2.count('1') % 2 == 0:
        s3 = '1' + s2 + '00'
    else:
        s3 = '10' + s2 + '1'
    return int(s3, 2)


print(alg(123456789))
c = 0
for i in range(100_000_000, 1000_000_000):
    if alg(i) == 21:
        c += 1
print(c)