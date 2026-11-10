macierz = [[1, 2, 4, 6], [2, 3, 4, 5], [12, 3, 4, 5]]
skalar = 3

wynik = []
for wiersz in macierz:
    nowy_wiersz = []
    for liczba in wiersz:
        nowy_wiersz.append(liczba * skalar)
    wynik.append(nowy_wiersz)

print(wynik)
