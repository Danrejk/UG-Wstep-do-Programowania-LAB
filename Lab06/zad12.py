punkty = {"Jan": 50, "Anna": 70, "Marta": 20, "Piotr": 40}

suma = 0
for imie, pkt in punkty.items():
    if imie[0] == "J" or imie[0] == "P":
        suma += pkt

print(suma)
