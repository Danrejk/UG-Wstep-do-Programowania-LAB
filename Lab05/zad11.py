n = int(input("Podaj liczbę: "))

cyfry = ["", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
naste_liczby = ["dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
dziesiate_liczby = ["", "", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
setne_liczby = ["", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset", "osiemset", "dziewięćset"]

if n == 0:
    wynik = "zero"
else:
    czesci = []
    s = n // 100
    d = (n % 100) // 10
    c = n % 10

    if s > 0:
        czesci.append(setne_liczby[s])
    if d == 1:
        czesci.append(naste_liczby[c])
    else:
        if d > 1:
            czesci.append(dziesiate_liczby[d])
        if c > 0:
            czesci.append(cyfry[c])

    wynik = " ".join(czesci)

print(wynik)
