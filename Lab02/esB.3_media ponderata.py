import math

voto_1 = int(input("Inserisci primo voto:"))
cfu_1 = int(input("Inserisci primo cfu:"))

voto_2 = int(input("Inserisci secondo voto:"))
cfu_2 = int(input("Inserisci secondo cfu:"))

voto_3 = int(input("Inserisci terzo voto:"))
cfu_3 = int(input("Inserisci terzo cfu:"))

media = ( voto_1*cfu_1 + voto_2*cfu_2 + voto_3*cfu_3 ) / ( cfu_1 + cfu_2 + cfu_3)

print(f"Media ponderata arrotondata a 2 decimali: {media:.2f}")
print(f"Media ponderata arrotondata intero: {int(round(media))}")
print(f"Media ponderata arrotondata a 2 decimali: {media * 100 / 30:.2f}")   