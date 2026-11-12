lista = ["jabłko", "banan", "jabłko", "wiśnia", "banan"]

bez_duplikatow = []
for owoc in lista:
    if owoc not in bez_duplikatow:
        bez_duplikatow.append(owoc)

zbior1 = set(bez_duplikatow)
zbior2 = set(lista)

print(zbior1)
print(zbior2)
