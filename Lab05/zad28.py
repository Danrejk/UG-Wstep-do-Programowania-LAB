listy = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 1, 2]]

unikalne = []
for podlista in listy:
    for liczba in podlista:
        if liczba not in unikalne:
            unikalne.append(liczba)

unikalne.sort()
print(unikalne)
