import random

lista = []
liczba = random.randint(1, 10)
for _ in range(10):
    lista.append(liczba)
    liczba += random.randint(1, 10)

print(lista)
