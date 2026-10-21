boki = int(input("Podaj liczbę boków: "))

if boki < 3:
    print("Taka figura nie istnieje.")
elif boki == 3:
    print("Trójkąt")
elif boki == 4:
    print("Czworokąt")
else:
    print("Wielokąt")
