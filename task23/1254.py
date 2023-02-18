def f(c, k):
    if k == 9:
        return s.add(c)
    f(c * 2, k + 1)
    f(c * 2 + 1, k + 1)


s = set()
f(1, 0)
print(len(s))