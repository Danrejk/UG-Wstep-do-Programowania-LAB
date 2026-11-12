lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

wspolne = list(set(lista1) & set(lista2))
print(wspolne)

print("nie trzeba iterować, i poprostu tak ładnie sie bierze te wspólne elementy z listy 1 i 2, i zamienia na listę")
print("pewnie to jest też jakoś zoptymalizowane, chociaż nie wiem bo to python, ale wsm fajny trik, nie pomyślałbym")
print("tak czy siak pytanie jest o efektownośc, a nie o efektywność, więc jest to efektywne definitywnie, wystarczy zobaczyć - ładny clean code")
