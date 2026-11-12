tekst = "Hello World!"
licznik = {}

for litera in tekst:
    if litera in licznik:
        licznik[litera] += 1
    else:
        licznik[litera] = 1

print(licznik)
