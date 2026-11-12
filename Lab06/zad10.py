zdanie = "Programowanie jest fajne, programowanie jest proste"

slowa = zdanie.lower().replace(",", "").split()
licznik = {}

for slowo in slowa:
    if slowo in licznik:
        licznik[slowo] += 1
    else:
        licznik[slowo] = 1

print(licznik)
