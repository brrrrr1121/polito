A  = "CCGTAGCATGGCTTACGATTGACCGTATGCAAGTCG"

C,G,T,A = 0,0,0,0

DNA = input("Il filamento di DNA: ").upper()

lun = len(DNA)

for i in range(lun):
    if DNA[i] not in "ACGT":
        print(f"Carratere non valido '{DNA[i]}' in posizione {i}")
        break

for i in range(lun):
    if DNA[i] == 'G':
        G +=1
    if DNA[i] == 'C':
        C +=1
    if DNA[i] == 'T':
        T +=1
    if DNA[i] == 'A':
        A +=1

print(f"Lunghezza: {lun} basi\n"
      f"A: {A:3} ({A/lun:.1%})\nC: {C:3} ({C/lun:.1%})\nG: {G:3} ({G/lun:.1%})\nT: {T:3} ({T/lun:.1%})\n"
      f"Contenuto GC: {(G+C)/lun:.1%}")

compl = ""

for i in range(lun):
    if DNA[i] == 'G':
        compl += 'C'
    if DNA[i] == 'C':
        compl += 'G'
    if DNA[i] == 'T':
        compl += 'A'
    if DNA[i] == 'A':
        compl += 'T'

print(f"Filamrnto: {DNA}\nComplemento: {compl}")

print(f"Approfondimento:\nA: {DNA.count("A"):3}\nC: {DNA.count("C"):3}\nG: {DNA.count("G"):3}\nT: {DNA.count("T"):3}")