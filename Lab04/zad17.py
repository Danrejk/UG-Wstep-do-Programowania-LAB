for n in range(100, 1000):
    c1 = n // 100
    c2 = (n // 10) % 10
    c3 = n % 10
    if c1 < c2 < c3:
        print(n)
