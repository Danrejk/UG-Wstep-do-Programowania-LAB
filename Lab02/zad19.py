a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

if a + b > c and a + c > b and b + c > a:
    print("Z tych boków można utworzyć trójkąt.")
else:
    print("Z tych boków nie można utworzyć trójkąta.")
