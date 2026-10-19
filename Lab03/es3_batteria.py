livello = 100

while True:
  consumo = input("Consumo orario (%):") 
  
  if consumo.isdigit():

    if int(consumo) <= 100 and int(consumo) >= 1:
      consumo = int(consumo)
      break
    else:
      print("Errore: il consumo deve essere un numero intero tra 1 e 100")

  elif not consumo.isdigit():
    print("Errore: il consumo deve essere un numero")


while True:
  ore = input("Ore di utilizzo:") 
  
  if ore.isdigit():

    if int(ore) >= 1:
      ore = int(ore)
      break
    else:
      print("Errore: le ore deve essere un numero interop maggiore del 0")

  elif not ore.isdigit():
    print("Errore: le ore di utilizo deve essere un numero")


for h in range(ore + 1):
  if livello > 0:
    print(f"Ora {h} -> {livello} %")
    livello -= consumo
  elif livello <= 0:
    print(f"Ora {h} -> 0 % Batteria scarica!!")