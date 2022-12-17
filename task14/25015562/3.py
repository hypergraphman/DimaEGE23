from string import ascii_uppercase, digits

def n_to_p(n, p):
    r = ''
    a = digits + ascii_uppercase
    while n > 0:
        d = a[n % p]
        r = d + r
        n //= p
    return r

n = 343 ** 1515 - 6 * 49** 1520 + 5*49**1510 - 3 * 7 ** 1530 - 1550
print(n_to_p(n, 7).count("0"))