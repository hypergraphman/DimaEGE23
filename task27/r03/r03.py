n, *a = map(int, open('27a.txt'))
k = 43
max_sum = 0
for i in range(n):
    for j in range(i, n):
        t = a[i: j + 1]
        if sum(t) % k == 0:
            if sum(t) > max_sum:
                max_sum = sum(t)
                min_len = len(t)
            elif sum(t) == max_sum:
                if len(t) < min_len:
                    min_len = len(t)
print(min_len)