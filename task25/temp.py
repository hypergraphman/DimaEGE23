import time


def d1(n):
    r = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)

print(d1(100))


# def d(n):
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             yield i
#             if i * i != n:
#                 yield n // i
#
#
# a = []
# k = time.time()
# for i in range(1_000_000, 1_100_000):
#     a.append(d1(i))
#     # print(i)
# print(time.time() - k)