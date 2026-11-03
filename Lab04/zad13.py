for n in range(1, 800):
    dzielniki = 0
    for d in range(1, n + 1):
        if n % d == 0:
            dzielniki += 1
            if dzielniki > 2:
                break
    if dzielniki <= 2:
        print(n)
