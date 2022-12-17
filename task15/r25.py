for a in range(1, 1000):
    is_a = True
    for x in range(1,1000):
        if not((x & 125 != 1) or ((x & 34 == 2) <= (x & a ==0))):
            is_a = False
            break
    if is_a:
        print(a)
        break