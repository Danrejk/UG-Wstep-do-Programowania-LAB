lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8, 9]

wynik = []
i = 0
j = 0

while i < len(lista1) and j < len(lista2):
    if lista1[i] <= lista2[j]:
        wynik.append(lista1[i])
        i += 1
    else:
        wynik.append(lista2[j])
        j += 1

wynik.extend(lista1[i:])
wynik.extend(lista2[j:])

print(wynik)
