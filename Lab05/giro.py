tempi = []
i = 1

while True:
    t = input(f"Tempo giro {i}: ")
    if t == " ":
        break
    t = float(t)
    tempi.append(t)
    i += 1

medio = sum(tempi) / len(tempi)

print("Tempi:", tempi)
print(f"Tempo medio: {medio:.2f}")


print("Giro piu veloce della media:")

for i,t in enumerate(tempi):
    if t < medio:
        print(f"Giro {i+1}: {t}")

max = 0
min = 0

for i in range(1,len(tempi)):
    if tempi[i] > tempi[max]:
        max = i

    if tempi[i] < tempi[min]:
            min = i

print(f"Giro migliore: Giro {min+1}, {tempi[min]}")
print(f"Giro migliore: Giro {max+1}, {tempi[max]}")