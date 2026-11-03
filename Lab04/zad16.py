n = int(input("Podaj n: "))

mozna = False
for a in range(int(n ** 0.5) + 1):
    for b in range(a, int(n ** 0.5) + 1):
        if a * a + b * b == n:
            mozna = True
            break
    if mozna:
        break

if mozna:
    print("TAK")
else:
    print("NIE")
