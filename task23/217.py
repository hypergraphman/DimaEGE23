from functools import lru_cache


@lru_cache
def f(x, y, ex, ey):
    if x > ex or y > ey:
        return 0
    if x == ex and y == ey:
        return 1
    return f(x + 1, y, ex, ey) + f(x * 2, y, ex, ey) + f(x, y + 3, ex, ey)


print(f(1, 0, 17, 27))