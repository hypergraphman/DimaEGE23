f = open('24-239.txt')
# f = open('test.txt')
s = f.readline() + '  '


k = 0
i = 0
mx = 0
while i < len(s) - 2:
    c1, c2, c3 = s[i], s[i + 1], s[i + 2]
    if c1 + c2 + c3 == 'YZZ':
        k += 3
        mx = max(mx, k)
        i += 3
    elif c1 + c2 == 'XY' or c1 + c2 == 'YZ':
        k += 2
        mx = max(mx, k)
        i += 2
    else:
        i += 1
        k = 0
print(mx)
