mn_a = 55
mn_n_with_a = None
mx_a = 0
mx_n_with_a = None

for a in range(0, 55):
    n = (int("Z", 36) * 55**3 + a * 55**2 + int("Y", 36) * 55 + int("X", 36)
         - 2 * 55**3 - int("X", 36) * 55**2 - a * 55 - int("Y", 36))
    if n % 29 == 0:
        print(a, n)
        if a < mn_a:
            mn_a = a
            mn_n_with_a = n
        if a > mx_a:
            mx_a = a
            mx_n_with_a = n
print(mx_a, mn_a)
print(mx_n_with_a - mn_n_with_a)
