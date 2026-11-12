uczen1 = {"matematyka": 4, "biologia": 5}
uczen2 = {"matematyka": 5, "biologia": 3}

for przedmiot in ["matematyka", "biologia"]:
    ocena1 = uczen1[przedmiot]
    ocena2 = uczen2[przedmiot]
    if ocena1 > ocena2:
        print(f"Na {przedmiot} uczeń 1 jest lepszy")
    elif ocena2 > ocena1:
        print(f"Na {przedmiot} uczeń 2 jest lepszy")
    else:
        print(f"Na {przedmiot} obaj mają taką samą ocenę ({ocena1})")
