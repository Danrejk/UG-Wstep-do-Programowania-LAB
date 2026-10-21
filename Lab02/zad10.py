a = 1
b = -5
c = 6

if a == 0:
    if b != 0:
        print("Liczba miejsc zerowych: 1")
    elif c == 0:
        print("Nieskończenie wiele miejsc zerowych")
    else:
        print("Liczba miejsc zerowych: 0")
else:
    delta = b**2 - 4 * a * c
    if delta > 0:
        print("Liczba miejsc zerowych: 2")
    elif delta == 0:
        print("Liczba miejsc zerowych: 1")
    else:
        print("Liczba miejsc zerowych: 0")
