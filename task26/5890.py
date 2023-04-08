f = open('26_5890.txt')
n, m = map(int, f.readline().split())

data = []

for i in range(n):
    x = int(f.readline())
    data.append(x)
data.sort()
k = 0
trucks = []
while data:
    trucks.append(0)
    for i in range(len(data) - 1, -1, -1):
        if trucks[k] + data[i] <= m:
            trucks[k] += data[i]
            data.pop(i)
    k += 1

print(k, trucks[-2], trucks[-1])


