a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

tekst = str(a + b)
licznik = 0
while tekst != "":
    licznik += 1
    tekst = tekst[1:]

print(licznik)
