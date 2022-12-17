from string import ascii_uppercase, digits


def n_to_p(n, p):
    r = ''
    a = digits + ascii_uppercase
    while n > 0:
        d = a[n % p]
        r = d + r
        n //= p
    return r


n = 51 * 7 ** 12 - 7 ** 3 - 22
print(sum(map(int, n_to_p(n, 7))))
