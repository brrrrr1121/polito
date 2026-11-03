while True:
    n = input("N:")
    if n.isdigit():
        break
    else:
        print("Errore: Devi inserire un nuemro intero positivo!!")

n = int(n)

for i in range (1,n+1):
    if n % i == 0:
        print(i)

