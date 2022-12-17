from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alf = digits + ascii_uppercase
    while n > 0:
        d = alf[n % p]
        r = d + r
        n //= p
    return r


n = 216**1315 - 4 * 36**1502 + 5 * 36 ** 1510 - 3 * 6 **1331 - 253
print(n_to_p(n,6).count("0"))
