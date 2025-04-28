#Richiesta di input
testo = input("""Inserisci il tuo testo qui: 
>>>> """)
da_sostituire = input("Inserisci i caratteri che vuoi sostituire: ")
sostituti = input("Inserisci i caratteri sostitutivi: ")

#creazione dizionario con comprehension
d = {ord(da_sostituire[i]) : None if i >= len(sostituti) else ord(sostituti[i]) for i in range(len(da_sostituire)) }

#traduzione del testo
testo_tradotto = testo.translate(d)

#output del testo tradotto
print()
print(testo_tradotto)