data = list(map(int, open('17-1.txt').readlines()))
avg = sum(data) / len(data)
k = 0
mx = -10**10
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if ((p1 < avg or p2 < avg)
       and (p1 % 3 == 0 and p1 % 5 and p1 % 11 and p1 % 19
       or p2 % 3 == 0 and p2 % 5 and p2 % 11 and p2 % 19)):
        k += 1
        mx = max(mx, p1 + p2)
print(k, mx)