while True:
    try:
        acconto = float(input("Acconto in euro:"))
        if acconto <= 0:
            print("Errore: l'acconto deve essere maggiore di 0")
        else:
            break
    except ValueError:
        print("Errore: inserisci u numero")

print(acconto,"euro")