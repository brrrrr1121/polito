import math

print("Equazione di secondo grado: ax^2 + bx + c = 0 \n")

while True:
    try:
        a = float(input("inserisci a:"))
        b = float(input("inserisci b:"))
        c = float(input("inserisci c:"))
        break

    except ValueError:
        print("-" * 5 + "Erroei: i coefficenti devono essere numeri" + "-" * 5)

print(f"\nEquazione di secondo grado: {a}x^2 + {b}x + {c} = 0 \n")

if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
        DEL = math.sqrt(delta)
        x1 = (-b + DEL) / (2*a)
        x2 = (-b - DEL) / (2*a)
        print(f"Le soluzioni sono: {x1:.2f} e {x2:.2f}")
    elif delta == 0:
        x = -b/(2*a)
        print(f"La soluzione è: {x:.2f}")
    elif delta < 0:
        print("Nessuna soluzione reale")
elif a == 0 and b != 0:
    x = -c/b
    print(f"Equazione è di primo grado, la soluzione è: {x:.2f}")
elif a == 0 and b == 0 and c != 0:
   print("Nessuna soluzione")
elif a == 0 and b == 0 and c == 0:
    print("Infiniti soluzioni")