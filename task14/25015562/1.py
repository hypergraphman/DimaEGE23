from string import digits, ascii_uppercase

def n_to_p(n, p):
    r = ''
    alf = digits + ascii_uppercase
    while n > 0:
        d = alf[n % p]
        r = d + r
        n //= p
    return r

n = 11*5**65 + 18*15**38 + 14*15**17 + 19*15**11+18338
print(len(set(n_to_p(n, 15))))
