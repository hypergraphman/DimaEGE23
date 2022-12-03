from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alf = digits + ascii_uppercase
    while n > 0:
        d = alf[n % p]
        r = d + r
        n //= p
    return r


# def test():
#     assert n_to_p(100, 2) == '1100100'
#     assert n_to_p(194, 5) == '1234'
#     assert n_to_p(255, 16) == 'FF'


if __name__ == '__main__':
    print(n_to_p(49**7 + 7**21 - 7, 7).count('6'))
