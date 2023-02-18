def f(c, e):
    if c < e:
        return 0
    if c == e:
        return 1
    if c > e:
        return f(c - 1, e) + f(c // 2, e)


print(f(int('100001', 2), 4))