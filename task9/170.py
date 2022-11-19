data = open('170.txt').readlines()
print(data)
count = 0
for line in data:
    nums = list(map(int, line.split()))
    set_nums = set(nums)
    if len(set_nums) == 5:
        t = sum(nums) - sum(set_nums)
        if (sum(set_nums) - t) / 4 <= 2 * t:
            count += 1
print(count)