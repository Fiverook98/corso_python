#Richiesta della base e dall'altezza
base = int(input("Inserisci la base del tuo rettangolo  : "))
altezza = int(input("Inserisci l'altezza del tuo rettangolo: "))
char_bor= '*'
char_in = ' '

#Disegno delle linee
linea_bor = char_bor * base
linea_in = char_bor + char_in * (base - 2) + char_bor

#ciclo per il rettangolo
for i in range(altezza):
    if i == 0 or i == altezza - 1:
        print(linea_bor)
    else:
        print(linea_in)
