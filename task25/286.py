from re import fullmatch

for x in range(2023, 10**9, 2023):
    if fullmatch(r'1\d*1\d*1\d', str(x)) and x % 19 == 0 and x % 6 == 0:
        print(x, x // 2023)