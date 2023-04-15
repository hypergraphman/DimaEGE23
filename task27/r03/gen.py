from random import randint
f = open('27b.txt', 'w')
f.write('100000\n')
for _ in range(100000):
    f.write(str(randint(1, 10000)) + '\n')