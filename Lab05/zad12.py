slowo = input("Podaj słowo: ")
wzorzec = input("Podaj wzorzec: ")

znaleziono = False
n = len(slowo)
m = len(wzorzec)

for i in range(n - m + 1):
    zgodne = True
    for j in range(m):
        if slowo[i + j] != wzorzec[j]:
            zgodne = False
            break
    if zgodne:
        znaleziono = True
        break

if znaleziono:
    print("TAK")
else:
    print("NIE")
