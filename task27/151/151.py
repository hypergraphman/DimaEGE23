# 1146648
n, k, *a = map(int, open("27-151b.txt"))

a37 = [0] * 100
na37 = [0] * 100

count = 0
for i in range(len(a)):
    if i > k:
        if a[i - k - 1] % 37 == 0:
            a37[a[i - k - 1] % 100] -= 1
        else:
            na37[a[i - k - 1] % 100] -= 1
    if a[i] % 37 == 0:
        a37[a[i] % 100] += 1
        count += na37[a[i] % 100]
    else:
        na37[a[i] % 100] += 1
        count += a37[a[i] % 100]
print(count)