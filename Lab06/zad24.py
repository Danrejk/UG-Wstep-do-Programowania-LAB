A = {4, 5, 6}
lista = [1, 2, 3]

try:
    A.add(lista)
except TypeError as e:
    print(e)
    print("Zbiory mogą przechowywać wyłącznie ele niezmienne. Lista jest zmienna, wiec nie można jej w zbiorze.")

krotka = tuple(lista)
A.add(krotka)
print(A)
