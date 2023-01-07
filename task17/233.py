data = list(map(int, open("17-1.txt").readlines()))
avr = sum(data)/len(data)
k = 0
mx = -10**10
for i in range(2, len(data)):
    p1, p2, p3 = data[i - 2] , data[i - 1], data[i]
    if ((p1 < avr or p2 < avr or p3 < avr) and (("2" in str(p1) and "2" in str(p2)) or ("2" in str(p1) and "2" in str(p3)) or ("2" in str(p2) and "2" in str(p3)))):
        k += 1
        mx = max(mx, p1 + p2 + p3)

print(k, mx)
        