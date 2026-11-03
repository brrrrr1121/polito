playlist = ["Bohemian","Imagine","Hotel","Yesterday","Wonderwall"]

while True:
    print("1) Mostra\n2) Aggiungi\n3) Inserisci\n0) Esci")
    n = int(input("Scelta:"))
    if n == 0:
        break
    if n == 1:
        for i,k in enumerate(playlist):
            print(f"{i+1}. {playlist[i]}")
    elif n == 2:
        titolo = input("Titolo:")
        playlist.append(titolo)
    elif n == 3:
        titolo = input("Titolo:")
        posizione = int(input("Posizione:"))
        playlist.insert(posizione-1,titolo)

print("Primo brano", playlist[0])
print("Ultimo brano", playlist[-1])