a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

for _ in range(max(a, b) + 1):
    if b == 0:
        break
    a, b = b, a % b

print(a)
