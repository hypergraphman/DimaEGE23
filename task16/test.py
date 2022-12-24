def f(n):
    if n < 1:
        return 1
    if n % 2:
        return f(n // 2) + n
    return n * f(n*2)


for i in range(1000):
    try:
        t = f(i)
        if t > 1000:
            print(i, t)
            break
    except:
        pass
