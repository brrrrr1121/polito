somma_voto = 0
somma_cfu = 0
i = 1

while True:

  while True:          
    voto = input(f"{i} voto ('fine' per terminare): ")
    if voto == "fine" and i == 1:
      print("Nessun voto inserito")
    elif voto == "fine":
      break
    elif not voto.isdigit() or int(voto) < 18 or int(voto) > 30:
      print("Errore: il voto deve essere un numero intero tra 18 e 30")
    else:
      break

  if voto == "fine":
    break

  while True:
    cfu = input(f"{i} CFU: ")
    if not voto.isdigit() or int(cfu) <= 0:
      print("Errore: il cfu deve essere un numero maggiore del 0")
    else:
      break

  somma_voto += int(voto) * int(cfu)
  somma_cfu += int(cfu)

  i+=1

media_ponderata = somma_voto / somma_cfu

print(f"Media ponderata: {media_ponderata:.1f}")
  

  