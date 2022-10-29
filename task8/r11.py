from itertools import product

c = 0
for letters in product('ШКОЛА', repeat=3):
    word = ''.join(letters)
    if word.count('К') == 1:
        c += 1
print(c)