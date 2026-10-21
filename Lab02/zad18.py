temp = float(input("Podaj temperaturę w stopniach Celsjusza: "))

if temp < 0:
    print("mróz")
elif temp <= 15:
    print("chłodno")
elif temp <= 25:
    print("ciepło")
else:
    print("gorąco")
