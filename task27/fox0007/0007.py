data = []
with open("27_A.txt") as f:
    n = int(f.readline())
    for i in range(n):
        num, k = map(int, f.readline().split())
        data.append([num, (k+24)//25])


for i in range(n):
    st = 0
    for j in range(n):
        st += data[j][1] * abs(data[i][0] - data[j][0])
    print(i, st)