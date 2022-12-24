from time import time
from functools import lru_cache


@lru_cache(maxsize=500)
def f(n):
    if n <= 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


for i in range(100, 100500, 100):
    f(i)

print(f(100500))

a = []
for i in range(100500 + 1):
    if i <= 2:
        a.append(1)
    else:
        a.append(a[i - 1] + a[i - 2])
print(a[100500])
