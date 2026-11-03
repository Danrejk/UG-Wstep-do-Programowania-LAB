n = int(input("Podaj liczbę: "))

m = 0
suma = 0
while suma + (m + 1) <= n:
    m += 1
    suma += m

print(m)
