persone = input("Quante prtsone?")

while not persone.isdigit() or int(persone) < 1:
    print("Errore: inserisci un numero maggiore di 0")
    persone = input("Quante persone?")

persone = int(persone)
print(persone, "persone")
