cmds = (lambda x: x + 2, lambda x: x + 3, lambda x: x * 2)
win = 30
a = [set(range(win,100))] + [set() for i in range(win - 1, 0, -1)]
for i in range(win - 1, 0, -1):
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

print(*sorted(a[2]))
print(*sorted(a[3]))
print(*sorted(a[4]))