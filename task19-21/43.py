cmds = (lambda x: x + 1, lambda x: x + 2, lambda x: x + 3, lambda x: x * 2)
a = [set(range(34,100))] + [set() for i in range(33, 0, -1)]
for i in range(33, 0, -1):
    t = []
    for cmd in cmds:
        for j, s in enumerate(a):
            if cmd(i) in s:
                t.append(j)
                break
    even = tuple(filter(lambda x: x % 2 == 0, t))
    if even:
        a[min(even) + 1].add(i)
        continue
    odd = tuple(filter(lambda x: x % 2, t))
    a[max(odd) + 1].add(i)

print(*a[2])
print(min(a[3]), max(a[3]))
print(*a[4])