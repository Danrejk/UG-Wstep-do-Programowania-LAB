slowo = input("Podaj słowo: ")

samogloski = "aeiouyAEIOUY"
licznik = 0
for znak in slowo:
    if znak in samogloski:
        licznik += 1

print(licznik)
