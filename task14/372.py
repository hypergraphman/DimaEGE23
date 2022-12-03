for x in range(0, 10):
    p1 = int(f'12{x}34')
    p2 = int(f'1234{x}')
    n = (p1 + 9 + 2 * p2 + 3)
    print(n)
