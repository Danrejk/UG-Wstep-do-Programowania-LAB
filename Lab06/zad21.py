A = {1, 3, 5, 7, 9}

if 4 in A:
    print("4 jest w A")
else:
    print("4 nie ma w A")

liczba = int(input("Podaj liczbe: "))

if liczba in A:
    print(f'{liczba} jest w  A')
else:
    print(f"{liczba} nie było w A, ale już jest ;)")
    A.add(liczba)

print(A)
