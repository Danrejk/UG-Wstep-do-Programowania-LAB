slownik = {"a": 1, "b": 2, "c": 3}

zamieniony = {}
for klucz, wartosc in slownik.items():
    zamieniony[wartosc] = klucz

print(zamieniony)
