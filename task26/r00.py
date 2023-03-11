for i in range(0, 21):
    with open(f'26-{i}.txt') as f:
        v, n = map(int, f.readline().split())
        a = list(map(int, f.readlines()))
    a.sort()

    k = 0
    while k < n and v - a[k] >= 0:
        v -= a[k]
        k += 1
    print(i, k, end=' ')

    v += a[k - 1]
    while k < n and v - a[k] >= 0:
        k += 1
    print(a[k - 1])