while True:
    try:
        n = int(input("Numero di articolo: "))
        break
    except ValueError:
        print("Errore: devi inserire un numero!!\n")

matrix = []

for i in range(n):

    salta = False
    row = []
    
    for k in ["nome","prezzo","quantita"]:
        a = input(f"Articolo {i+1} - {k}: ")
        if k == "nome":
            row.append(a)
        else:
            while True:
                try:
                    row.append(float(a))
                    break
                except ValueError:
                    a = input(f"Errore: devi inserire un numero!!\nArticolo {i+1} - {k}: ")

    if row[2] == 0:
        continue

    row.append(row[1]*row[2])
    
    matrix.append(row)

tot = sum(row[3] for row in matrix )
pezzi = sum(row[1] for row in matrix )

print(f"{"Articolo":<12}{"Qta":>3}{"Prezzo":>7}{"Importo":>9}\n{"-"*31}")

for row in matrix:
    print(f"{row[0]:<12}{row[1]:>3}{row[2]:>7.2f}{row[3]:>9.2f}")

print(f"{"-"*31}\nTOTALE{tot:>27.2f}\nPezzi:{pezzi}")

