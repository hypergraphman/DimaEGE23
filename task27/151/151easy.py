n, k, *a = map(int, open("27-151b.txt"))

count = 0
for i in range(len(a) - 1):
    for j in range(i + 1, min(i + k + 1, n)):
        if (a[i] - a[j]) % 100 == 0 and (a[i] % 37 == 0) != (a[j] % 37 == 0):
            count += 1

print(count)

