macierz = [
    [1, 2, 3],
    [4, 5, 6]
]

transponowana = []
for j in range(len(macierz[0])):
    nowy_wiersz = []
    for i in range(len(macierz)):
        nowy_wiersz.append(macierz[i][j])
    transponowana.append(nowy_wiersz)

print(transponowana)
