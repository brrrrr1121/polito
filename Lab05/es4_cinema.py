sala = []

lettere = 'ABCDE'

for i in range(5):
    fila = []
    for k in range (8):
        fila.append(".")
    sala.append(fila)

occupati = ["A3","A4","B2","B7","C4","C5","C6","D1","E8"]

for i in range(len(occupati)):
    sala[lettere.index(occupati[i][0])][int(occupati[i][1])-1] = 'X'

print(*sala,sep="\n")


def stampa(sala):
    print("  1 2 3 4 5 6 7 8")
    for i,fila in enumerate(sala):
        print(lettere[i]," ".join(fila),"\n")

while True:
    stampa(sala)
    prenota = input("Posto da prenotare:").upper()
    if prenota == "":
        stampa(sala)
        break
    elif sala[lettere.index(prenota[0])][int(prenota[1])-1] == 'X':
        print("Il posto e gia occupato")
    else:
        sala[lettere.index(prenota[0])][int(prenota[1])-1] = 'X'
        print("Prenotato il posto ",prenota)

mas = 0
for i,c in enumerate(lettere):
    print(f"Fila {c}: {sala[i].count(".")} posti liberi")
    mas = max(mas,sala[i].count("."))


print("Fila con piu posti:")
for i,c in enumerate(lettere):
    if sala[i].count(".") == mas:
        print(c)