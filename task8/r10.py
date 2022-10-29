from itertools import permutations

words = set()
for letters in permutations('КАПКАН'):
    word = ''.join(letters)
    if 'КК' not in word and 'АА' not in word:
        words.add(word)
print(len(words))