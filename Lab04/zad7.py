rozmiar = 6

for i in range(1, rozmiar + 1):
    print(" " * (rozmiar - i) + " ".join(["*"] * i))

pien = ((2 * rozmiar - 1) - 5) // 2
print(" " * pien + "|___|")
