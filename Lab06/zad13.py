zwierzeta = {"kot": 3, "pies": 2, "ryba": 1, "ptak": 4}

do_usuniecia = [klucz for klucz, wartosc in zwierzeta.items() if wartosc < 3]

for klucz in do_usuniecia:
    del zwierzeta[klucz]

print(zwierzeta)
