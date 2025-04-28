from calcolatrice_fun  import *
from operazioni import *

#avvio del ciclo

flag = True
while flag:
        
    #Richiesta dati
    a,b,op = richiesta()
    
    risultato = calcolatrice(a, b, op)
    
    #Stampa il risultato
    print(risultato)
    
    nuova_operazione = input("Vuoi effettuare una nuova operazione si = [Y] no = [N]")

    #Richiesta terminazione ciclo
    if nuova_operazione.upper() == 'N':
        print("Arrivederci!")
        flag = False
    elif nuova_operazione.upper() == 'Y':
        print('Riavvio del programma in corso')
    else:
        print(f"Errore inserimento!!! Chiusura Programma {calcolatrice}!!!")
        flag = False