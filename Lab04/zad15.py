m = int(input("Podaj m: "))
n = int(input("Podaj n: "))

for i in range(1, m + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print()
