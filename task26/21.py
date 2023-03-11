with open('26-k1.txt') as f:
    v, n = map(int, f.readline().split())
    a = list(map(int, f.readlines()))
a.sort(reverse=True)
print(a[n])
print(sum(a[:n])*0.2)

