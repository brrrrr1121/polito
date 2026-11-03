while True:
    eta = input("La tua eta:")
    if eta.isdigit():
        break
    else:
        print("Errore: Devi inserire un nuemro intero positivo!!")

eta = int(eta)

settimana = ["lunedi","martedi","mercoledi","giovedi","venerdi","sabato","domenica"]

while True:
    giorno = input("Che giorno e oggi?:")

    if giorno in settimana:
        break
    else:
        print("Errore: Devi inserire un giorno della settimana (una stringa in minuscolo, senza accenti, ad esempio lunedi oppure domenica)!!")

if eta < 12:
    costo = 5
elif eta > 75:
    costo = 7
else:
    costo = 12

if giorno == "domenica":
    costo -= 2 

print(f"Devi pagare {costo} EURO")   