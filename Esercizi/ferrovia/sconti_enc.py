#Richiesta dati
costo = float(input("Inserisci il costo del biglietto: "))
categoria = input("""SELEZIONARE LA CATEGORIA DI APPARTENENZA:
[P,p] Pensionati
[S,s] Studenti  
[D,d] Disoccupati
>>>> """)

# Dichiarazione Categorie e sconti
sconti = {'P': 0.1, 'S': 0.15, 'D': 0.25}
categoria = categoria.upper()

# Controllo della categoria e calcolo dello sconto
if sconti.get(categoria):
    sconto = sconti[categoria]
    print(f"""Il costo del biglietto ha uno sconto del {sconto * 100}%
L'importo del biglietto è {costo * (1 - sconto):.2f}""")
else:
    print("Categoria non prevista")
    print(f"Il costo del biglietto è {costo:.2f}")