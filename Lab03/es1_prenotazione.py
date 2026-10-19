persone = input("Quante persone?\n")

while not persone.isdigit() or int(persone) < 1:
    print("Errore: inserisci un numero maggiore di 0")
    persone = input("Quante persone?\n")

persone = int(persone)
print("Prenotati", persone , "persone")

codice = input("Codice prenotazione (6 caratteri):")

while len(codice) != 6 or not codice.isalnum():
    print("Errore: il codice deve avere 6 caratteri, tra lettere e cifre")
    codice = input("Codice prenotazione (6 caratteri):")

print("Codice prenotazione:", codice)



while True:
    try:
        acconto = float(input("Acconto in euro:"))
        if acconto <= 0:
            print("Errore: l'acconto deve essere maggiore di 0")
        else:
            break
    except ValueError:
        print("Errore: inserisci u numero")

print(f"Acconto versato: {acconto:.2f} euro")