import math

n = int(input("N e Limiti:"))

is_primo = True

if n % 2 == 0:
    print(f"{n} non è primo: è divisibile per 2")
else:
    for i in range(3,int(math.sqrt(n)+1),2):
        if n % i == 0:
            print(f"{n} non è primo: è divisibile per {i}, (divisione: {i-1})")
            is_primo = False
            break

    if is_primo == True:
        print(f"{n} è un primo, (divisione: {i-1})")

print(f"I numeri primo minore del {n} sono:")

for k in range(2, n):
    
    is_primo = True

    for i in range(2,int(math.sqrt(k)+1)):
        if k % i == 0:
            is_primo = False
            break
        

    if is_primo:
        print(k)
