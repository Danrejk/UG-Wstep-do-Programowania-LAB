import random

wylosowana = int(random.random() * 100) + 1

while True:
    strzal = int(input("Podaj liczbę: "))
    if strzal > wylosowana:
        print("Za duża")
    elif strzal < wylosowana:
        print("Za mała")
    else:
        print("Zgadłeś!")
        break
