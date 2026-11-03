sum = 0

while True:
    is_valido = False
    codice = input("Codice EAN-13: ")
    if len (codice)<12:
        print(f"Errore: il codice ha {len(codice)} cifre, e troppo breve") 
    elif len(codice)>13:
        print(f"Errore: il codice ha {len(codice)} cifre, e troppo lungo") 
    else:
        for i in range(len(codice)):
            if not codice[i].isdigit():
                print(f"Errore: carratere '{codice[i]} in posizione {i+1}")
                break
            else:
                is_valido = True

    if is_valido == True:
        break

codice.replace(" ","").replace("-","")

print("Pos  Cifre  Peso  Prodotto")

for i in range(12):
    if i % 2 == 0:
        peso = 1
    else:
        peso = 3

    prodotto = int(codice[i]) * peso
    print(f"{i:3}{codice[i]:7}{peso:6}{prodotto:10}")

    sum += prodotto

controllo = controllo = 10 - sum % 10
controllo = str(controllo)

print(f"Somma: {sum}")

if len(codice)==12:
    print(f"Codice di controllo: {controllo}")
    codice += controllo

if len(codice) == 13:
    if codice[12] != controllo:
        print(f"odice di controllo: {controllo}          *codice di controllo errato {codice[12]}")
        codice = codice[:-1] + controllo

print(f"Codice completto: {codice}")