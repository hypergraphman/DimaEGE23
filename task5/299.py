for n in range(1, 1000):
    n1 = bin(n)[2:]
    if n1.count('1') % 2 == 0:
        n2 = n1[1:]
    else:
        n2 = "1" + n1 + "00"
    if n2.count('1') % 2 == 0:
        n3 = n2[1:]
    else:
        n3 = "1" + n2 + "00"
    r = int(n3, 2)
    if r > 100:
        print(n)
