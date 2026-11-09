LIMITE = 50
letture = [48,53,47,-1,72,50,61,-1,49,72]

scartate = 0

for i in range(len(letture)):
    if letture[i-scartate] <= 0:
        letture.pop(i-scartate)
        scartate += 1

print("Letture scartate: ",scartate)
print("Letture valide: ", letture)

multe = 0

for i,v in enumerate(letture):
    if letture[i] > LIMITE:
        print(f"Letture {i}: {v} km/h (+{v-LIMITE})")
        multe += 1

print(f"Multi: {multe} su {len(letture)} letture ({multe/len(letture):.2%})")

a = []
max = 0
for i in range(len(letture)):
    if letture[i] > max:
        max = letture[i]
        a.clear()
        a.append(i+1)
    elif letture[i] == max:
        a.append(i+1)

print(f"Velocita massima: {max} km/h, registrata {letture.count(max)} volte")
print("Altre letture:", a)
