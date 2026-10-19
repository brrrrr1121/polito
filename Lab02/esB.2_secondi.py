secondi_i = int(input("Secondi:"))

minuti = secondi_i // 60
secondi = secondi_i % 60
ore = minuti // 60
minuti = minuti % 60
giorni = ore // 24
ore = ore % 24

print(f"{secondi_i} secondi sono: {giorni} giorni, {ore} ore, {minuti} minuti, {secondi} secondi")