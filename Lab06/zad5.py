ceny = {"chleb": 4, "dżem": 3, "paliwo": 8, "jajka": 10}

nowe_ceny = {}
for produkt, cena in ceny.items():
    nowe_ceny[produkt] = cena * 1.10

print(nowe_ceny)
