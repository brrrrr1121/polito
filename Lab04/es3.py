n = int(input("N:"))

primo = True

for i in range(2,n):
    if n % i == 0:
        print(f"{n} non è primo: è divisibile per {i}")
        primo = False
        break

if primo == True:
    print(f"{n} è un primo")