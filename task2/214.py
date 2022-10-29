print("a b c d")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                if (a <= b) and (b != c) and (d <= a):
                    print(a, b, c, d)
