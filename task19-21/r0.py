cmds = (lambda x, y: (x + 1, y), lambda x, y: (x, y + 1), lambda x, y: (x * 2, y), lambda x, y: (x, y * 2))
win = 77
s = set()
for i in range(1, 200):
    for j in range(1, 200):
        if i + j >= win:
            s.add((i, j))
a = [s] + [set() for i in range(win - 1, 0, -1)]
# print(a)

for i in range(win - 1, 0, -1):
    for k in range(win - 1, 0, -1):
        p = (i, k)
        t = []
        for cmd in cmds:
            for j, s in enumerate(a):
                if cmd(*p) in s:
                    t.append(j)
                    break
        even = tuple(filter(lambda x: x % 2 == 0, t))
        if even:
            a[min(even) + 1].add(p)
            continue
        odd = tuple(filter(lambda x: x % 2, t))
        a[max(odd) + 1].add(p)

# print(a[0])
# print(a[1])
print(a[2])
print(a[3])
print(a[4])