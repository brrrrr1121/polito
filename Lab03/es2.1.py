import math

print("Equazione di secondo grado: ax^2 + bx + c = 0")

a = int(input("inserisci a:"))
b = int(input("inserisci b:"))
c = int(input("inserisci c:"))

print("\nEquazione di secondo grado: (", a,")x^2 +(", b,")x +(", c, ")= 0\n")

if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
        DEL = math.sqrt(delta)
        x1 = (-b + DEL) / (2*a)
        x2 = (-b - DEL) / (2*a)
        print("Le soluzioni sono:", x1, "e", x2)
    elif delta == 0:
        x = -b/(2*a)
        print("La soluzione è:", x)
    elif delta < 0:
        print("Non ci sono soluzioni reali")
elif a == 0 and b != 0:
    x = -c/b
    print("La soluzione è:", x)
else:
   print("Non ci sono soluzioni reali")