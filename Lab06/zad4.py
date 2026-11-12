uczniowie = {"Jan": 20, "Paweł": 22, "Donald": 18, "Dulka": 24}

for szukany_wiek in [22,23]:
    znaleziono = False
    for imie, wiek in uczniowie.items():
        if wiek == szukany_wiek:
            print(f"{szukany_wiek} lat: {imie}")
            znaleziono = True
            break
    if not znaleziono:
        uczniowie["John"] = szukany_wiek
