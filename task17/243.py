from string import digits, ascii_uppercase

data = list(map(int, open("17-243.txt").readlines()))
k = 0
mina = 10 ** 10


def f(n):
    r = ''
    alf = digits + ascii_uppercase
    while n > 0:
        d = alf[n % 8]
        r = d + r
        n //= 8
    return r


max133 = 1
for i in range(len(data)):
    if data[i] > max133 and data[i] % 133 == 0:
        max133 = data[i]

for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if (p1 > max133 or p2 > max133) and ("3" in f(p1) or "3" in f(p2)):
        k += 1
        mina = min(mina, p1 + p2)

print(k, mina)
