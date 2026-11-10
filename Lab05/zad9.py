lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 6, 7, 8, 9]

wspolny = False
for x in lista1:
    if x in lista2:
        wspolny = True
        break

if wspolny:
    print("TAK")
else:
    print("NIE")
