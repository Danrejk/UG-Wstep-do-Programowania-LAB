suma = 0
while True:
    liczba = int(input("Podaj liczbę: "))
    if liczba % 2 != 0:
        break
    suma += liczba

print(suma)
