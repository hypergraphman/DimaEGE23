def f(s, e, p):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s + 1, e, s) + f(s * 3, e, s) + (f(s + p, e, s) if p > 0 else 0)


print(f(2, 27, 0))