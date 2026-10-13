codice = input("Codice prenotazione (6 caratteri):")

while len(codice) != 6 or not codice.isalnum():
    print("Errore: il codice deve avere 6 caratteri, tra lettere e cifre")
    codice = input("Codice prenotazione (6 caratteri):")

print("Codice prenotazione:", codice)
