win = 77
lose = 97


def f(a, c, m):
    if a >= win:
        return c % 2 == m % 2
    if a > lose:
        return c % 2 != m % 2
    if c == m:
        return False
    moves = [f(a + 1, c + 1, m),
             f(a * 3, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, win):
    for m in range(1, 4 + 1):
        if f(s, 0, m):
            print(s, m)
            break