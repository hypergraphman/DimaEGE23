with open("26.txt") as f:
    n = map(int, f.readline())
    a = list(map(int, f.readlines()))
a.sort(reverse = True)

r = []

r.append(a[0])

for i in range(1, len(a)):
    if r[-1] - a[i] >= 3:
        r.append(a[i])

print(len(r), r[-1])

