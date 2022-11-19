for x in range(100):
    for y in range(100):
        for z in range(100):
            if 3 * x + y + 7 * z == 96 and x + 3* z == 36 and 2 * x + y + 6 * z == 80:
                print(x, y, z, x + y + z + 2)