n, *a = map(int, open('27_b.txt'))

k = 89
mx_s = 0
mn_len = float('inf')

tail_sum = [0] + [None] * (k - 1)
tail_ind = [0] * k
total_sm = 0
for ind, x in enumerate(a, start=1):
    total_sm += x
    r = total_sm % k
    if tail_sum[r] == None:
        tail_sum[r] = total_sm
        tail_ind[r] = ind

    ln = ind - tail_ind[r]
    s = total_sm - tail_sum[r]
    if s > mx_s:
        mx_s = s
        mn_len = ln
    elif s == mx_s:
        mn_len = min(mn_len, ln)

print(mn_len, mx_s)