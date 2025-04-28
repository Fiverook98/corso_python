
#Richiesta base e altezza
base = int(input("Inserisci la base del tuo rettangolo  : "))
altezza = int(input("Inserisci l'altezza del tuo rettangolo: "))
char_bo = '*'
char_in = ' '

#Ciclo per il rettangolo

for i in range(altezza):
    if i == 0 or i == altezza - 1:
        for j in range(base):
            print(char_bo,end = '')
    else:
        for j in range(base):
            if j == 0 or j == base - 1:
                print(char_bo,end = '')
            else: 
                print(char_in,end = '')
    print()
