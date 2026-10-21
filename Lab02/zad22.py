a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

if a == b and b == c:
    print("Trójkąt równoboczny")
elif a == b or a == c or b == c:
    print("Trójkąt równoramienny")
else:
    print("Trójkąt różnoboczny")
