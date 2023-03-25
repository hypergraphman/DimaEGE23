f = open('26_2580.txt')
n, start = map(int, f.readline().split())
reqs = []
for _ in range(n):
    b, e = map(int, f.readline().split())
    if e == 0:
        e = float('inf')
    reqs += [b, -e]
reqs.sort(key=lambda x: abs(x))
# print(reqs)
k = 0
i = 0
while abs(reqs[i]) <= start:
    if reqs[i] >= 0:
        k += 1
    else:
        k -= 1
    i += 1
end = start + 24 * 60 * 60 * 1000
mx_k = k
range_begin = 0
len_range = 0
while abs(reqs[i]) < end:
    if reqs[i] >= 0:
        k += 1
        if k > mx_k:
            mx_k = k
            len_range = 0
            range_begin = reqs[i]
        if k == mx_k:
            range_begin = reqs[i]
    else:
        k -= 1
        if k == mx_k - 1:
            len_range += abs(reqs[i] + range_begin)
    i += 1
print(mx_k, len_range)