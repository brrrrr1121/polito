originale = ["Bohemian","Imagine","Hotel","Yesterday","Wonderwall"]
playlist = list(originale)

while True:
    print("\n1) Mostra\n2) Aggiungi\n3) Inserisci\n4) Rimosso\n0) Esci\n")
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
    elif n == 4:
        try:
            titolo = input("Titolo:")
            playlist.remove(titolo)
        except ValueError:
            print(titolo,"non e nella playlist") 

    print("Playlist:",playlist)
    print("Originale:",originale)

print("Primo brano", playlist[0])
print("Ultimo brano", playlist[-1])

ordine = sorted(playlist)
print("In ordine:",ordine)