from re import fullmatch

data = list(map(int, open("17-346.txt").readlines()))
k = 0
maxa = -10**10
for i in range(2, len(data)):
    prz = 1
    p1, p2, p3 = data[i - 2], data[i - 1], data[i]
    digits = str(p1) + str(p2) + str(p3)
    p = 1
    for digit in digits:
        digit = int(digit)
        if digit % 2 == 0:
            p *= digit
    if p <= 2 * 10 ** 9 and fullmatch(r'25\d*2\d*', str(p)):
        k += 1
        maxa = max(maxa, p)
print(k, maxa)