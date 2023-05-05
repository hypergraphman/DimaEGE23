n, *a = map(int, open('27-152a.txt'))

c = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        p1, p2 = a[i], a[j]
        t = p1 * p2
        if t % 10**5 == 0 and t % 10**6 != 0:
            c += 1
print(c)