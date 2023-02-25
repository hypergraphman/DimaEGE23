from functools import lru_cache


@lru_cache(None)
def d1(n):
    r = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)


for i in range(321930, 654321 + 1, 315):
    if i % 2 != 0 and len(d1(i)) > 70:
        print(i, d1(i)[-1])