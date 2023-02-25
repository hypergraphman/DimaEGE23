from re import fullmatch

for i in range(2023, 10**10 + 1, 2023):
    if fullmatch(r'1\d2139\d*4', str(i)):
        print(i, i // 2023)