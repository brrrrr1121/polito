PREZZO_INTERO = 9
PREZZO_BAMBINO = 6.5

NUMERO_ADULTO = int(input("Numero di adulti:"))
NUMERO_BAMBINO = int(input("Numero di bambini:"))

SPESA_ADULTO = PREZZO_INTERO * NUMERO_ADULTO
SPESA_BAMBINO = PREZZO_BAMBINO * NUMERO_BAMBINO
SPESA_TOT = SPESA_ADULTO + SPESA_BAMBINO

print(f"Spesa per gli adulti è {SPESA_ADULTO:.2f} EURO e la spesa per i bambini è {SPESA_BAMBINO:.2f} EURO, la spesa totale è {SPESA_TOT:.2f} EURO")
