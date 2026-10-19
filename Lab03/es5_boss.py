import random

hp_eroe = 60
hp_boss = 60
i=0

while True:
    i += 1

    if hp_eroe < 1 and hp_boss < 1:
        print(f"Pareggio!! 0 contro 0!!")
        break

    if hp_eroe < 1:
        print(f"Il boss ti ha sconfitto. Hai perso!! {hp_boss} contro 0!!")
        break

    if hp_boss < 1:
        print(f"Hai sconfitto il boss! Hai vinto!! {hp_eroe} contro 0!!")
        break

    if i > 5:
        if hp_eroe == hp_boss:
            print("Turni finiti, pareggio!!")
        elif hp_eroe > hp_boss:
            print(f"Turni finiti, vinci ai punti, {hp_eroe} contro {hp_boss}!!")
        elif hp_eroe < hp_boss:
            print(f"Turni finiti, vince il boss, {hp_boss} contro {hp_eroe}!!")
        break 

    print(f"""Turno {i} di 5
Vita del boss: {hp_boss} | La tua vita: {hp_eroe}
1) Attacca
2) Difendi""")

    while True:
        scelta = input(f"Scelta ({i} turno):")
        if scelta == "1" or scelta == "2":
            break
        else:
            print("Scelta non valida: inserisci 1 o 2")

    if scelta == "1":
        danni_boss = random.randint(10,25)
        danni_eroe = random.randint(10,25)
        print(f"Hai inflitto {danni_eroe} danni al boss.\n"
            f"Il boss ti ha inflitto {danni_boss} danni.\n")
        hp_eroe -= danni_boss
        hp_boss -= danni_eroe

    if scelta == "2":
        print("Ti prepari a parere il corpo.\n"
            "Il boss attacca, ma ti sei difeso: nessuno danno\n")