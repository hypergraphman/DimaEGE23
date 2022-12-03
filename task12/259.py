line = '1' * 170 + '3' * 100 + '2' * 7
while '11' in line:
    line = line.replace('112', '4', 1)
    line = line.replace('113', '2', 1)
    line = line.replace('42', '3', 1)
    line = line.replace('43', '1', 1)
print(line)