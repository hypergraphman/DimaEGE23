def alg(n):
    s1 = f'{n:b}'
    if sum(map(int, s1)) % 2 == 0:
        s2 = f'{int(s1[1:], 2):b}'
    else:
        s2 = '1' + s1 + '00'
    if sum(map(int, s2)) % 2 == 0:
        s3 = f'{int(s2[1:], 2):b}'
    else:
        s3 = '1' + s2 + '00'
    return int(s3, 2)


print(alg(5))
i = 1
while alg(i) <= 100:
    i += 1
print(i)
