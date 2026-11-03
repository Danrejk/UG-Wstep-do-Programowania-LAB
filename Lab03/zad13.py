slowo = input("Podaj słowo: ")

odwrocone = ""
i = len(slowo) - 1
while i >= 0:
    odwrocone += slowo[i]
    i -= 1

print(odwrocone)
