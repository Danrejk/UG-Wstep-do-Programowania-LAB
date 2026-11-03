n = int(input("Podaj liczbę: "))

licznik = 0
i = 1
while i <= n:
    if n % i == 0:
        licznik += 1
    i += 1

print(licznik)
