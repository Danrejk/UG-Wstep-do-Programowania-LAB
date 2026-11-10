liczby = [4, 7, 2, 9, 6, 8]

unikalne = list(set(liczby))
unikalne.sort()
drugi = unikalne[-2]

print("wartość:", drugi, "indeks:", liczby.index(drugi))
