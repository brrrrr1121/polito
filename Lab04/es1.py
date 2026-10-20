primo = 7*60 + 30
ult = 19* 60
DEL = 30
i = 0
for t in range(primo,ult+1,DEL):
    ora = t // 60
    min = t % 60
    i+=1
    print(f"Corso {i:02d} - {ora:02d}:{min:02d}")
