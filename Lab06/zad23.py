import random

zbior = set()
while len(zbior) < 10:
    zbior.add(random.randint(1, 20))

print("Wylosowany zbiór:", zbior)

mniejsze_niz_10 = {x for x in zbior if x < 10}
print("Liczby mniejsze niż 10:", mniejsze_niz_10)
