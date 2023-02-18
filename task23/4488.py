def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        if c % 2 == 0:
            return f(c + 1, e) + f(c + 2, e) + f(c * 2, e)
        else:
            return f(c * 2, e)

print(f(1, 32))