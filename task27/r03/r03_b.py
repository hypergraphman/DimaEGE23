n, *a = map(int, open('27A_2900.txt'))
k = 1000
tail_sum = [0] + [None] * (k - 1)
tail_len = [0] * k
total_sum = 0
max_sum = 0
min_len = 10**10
for i, x in enumerate(a):
    total_sum += x
    r = total_sum % k
    if tail_sum[r]:
        cur_sum = total_sum - tail_sum[r]
        if cur_sum > max_sum:
            max_sum = cur_sum
            min_len = i - tail_len[r]
        elif cur_sum == max_sum:
            if i - tail_len[r] < min_len:
                min_len = i - tail_len[r]
    else:
        tail_sum[r] = total_sum
        tail_len[r] = i
print(max_sum)