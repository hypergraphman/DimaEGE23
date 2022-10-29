def alg(n):
    n1 = bin(n)[2:]
    if n % 2 == 0:
        n2 = "1" + n1 + "11"
    else:
        n2 = "11" + n1 + "0"
    r = int(n2, 2)
    return r


c = 0
for i in range(1, 1000):
    if 500 <= alg(i) <= 1000:
        c += 1
print(c)
