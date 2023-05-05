def count_5_2(n):
    count_2 = 0
    num = n
    while num % 2 == 0:
        count_2 += 1
        num //= 2
    count_5 = 0
    num = n
    while num % 5 == 0:
        count_5 += 1
        num //= 5
    return count_5, count_2


n, *a = map(int, open('27-152b.txt'))
t = [[0] * 7 for _ in range(7)]
c = 0
for el in a:
    c_5, c_2 = count_5_2(el)
    if c_2 > 5:
        c_2 = 6
    if c_5 > 5:
        c_5 = 6
    y = 5 - c_5
    if y < 0:
        y = 0
    x = 5 - c_2
    if x < 0:
        x = 0
    c += sum(t[y][x:])
    for y_i in range(y + 1, 7):
        c += t[y_i][x]
    t[c_5][c_2] += 1
print(c)