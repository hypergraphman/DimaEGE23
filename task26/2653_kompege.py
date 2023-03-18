import time

n, *a = map(int, open('26_2653.txt').read().split())
a.sort()
w = [False] * (sum(a) + 1)
w[0] = True
s = 0
start = time.time()
for x in a:
    w2 = w[::]
    for i in range(s + 1):
        if w[i]:
            w2[x + i] = w[i]
    w = w2
    s += x
print(time.time() - start)
print(w.count(False))