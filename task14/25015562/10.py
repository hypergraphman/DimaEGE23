from string import ascii_uppercase, digits


def n_to_p(n, p):
    r = ''
    a = digits + ascii_uppercase
    while n > 0:
        d = a[n % p]
        r = d + r
        n //= p
    return r


for n in range(6, 30):
    if n_to_p(29, n)[-1] == '5':
        print(n)
