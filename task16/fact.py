def fact(n):
    x = 1
    while n > 0:
        x = n * x
        n = n - 1
    return x


def rec_fact(n):
    if n == 0:
        return 1
    return n * rec_fact(n - 1)


print(fact(5000))
print(rec_fact(5000))
