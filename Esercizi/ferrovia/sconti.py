#Richiesta dati
costo = float(input("Inserisci il costo del biglietto: "))
categoria = input("""SELEZIONARE LA CATEGORIA DI APPARTENENZA:
[P,p] Pensionati
[S,s] Studenti  
[D,d] Disoccupati
>>>> """)

#Dichiarazione Categorie
list_cat = ['P','S','D']
non_pre = False

#Controllo della categoria
if categoria.upper() == list_cat[0]:
    sconto = .1
elif categoria.upper() == list_cat[1]:
    sconto = .15
elif categoria.upper() == list_cat[2]:
    sconto = .25
else:
    print("categoria non prevista")
    non_pre = True

#Comunicazione Importo da pagare

if not non_pre:
     print(f"""Il costo del biglietto ha uno sconto del {sconto * 100}%
L'importo del biglietto è {costo * (1 - sconto):.2f}""")
else:
    print(f"Il costo del biglietto è {costo:.2f}")