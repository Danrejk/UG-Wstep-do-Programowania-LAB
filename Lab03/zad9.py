b = int(input("Podaj liczbę dwójkową: "))

dziesietna = 0
waga = 1
while b > 0:
    dziesietna += (b % 10) * waga
    waga *= 2
    b //= 10

print(dziesietna)
