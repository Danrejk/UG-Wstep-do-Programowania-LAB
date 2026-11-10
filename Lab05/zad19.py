n = 3
macierz = [
    [1, 2, 1],
    [4, 5, 6],
    [7, 8, 9]
]

przekatna_tl = 0
for i in range(n):
    przekatna_tl += macierz[i][i]

przekatna_tr = 0
for i in range(n):
    przekatna_tr += macierz[i][-(i+1)]

print(przekatna_tl, przekatna_tr)
