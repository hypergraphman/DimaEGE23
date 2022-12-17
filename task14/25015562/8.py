from string import ascii_uppercase, digits


def n_to_p(n, p):
    r = ''
    a = digits + ascii_uppercase
    while n > 0:
        d = a[n % p]
        r = d + r
        n //= p
    return r


a = []
for x in range(1, 100):
    for y in range(1, 100):
        n = 2*7**x + 3*7**x+1 + 4*7**x+2 + 5*7**y +6*7**2*y
        t = sum(map(int, n_to_p(n, 7)))
        a.append(t)
print(a.count(5))