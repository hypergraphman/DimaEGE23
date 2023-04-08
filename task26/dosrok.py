f = open("26_1.txt")
k = int(f.readline())
n = int(f.readline())


data = []
for i in range(n):
    st, end = map(int, f.readline().split())
    data.append([st, end])

data.sort()

kam = [0]*(k+1)

c = 0
last = 0

for i in range(len(data)):
    for j in range(1, len(kam)):
        if kam[j] < data[i][0]:
            kam[j] = data[i][1]
            c += 1
            last = j
            break

print(c, last)

