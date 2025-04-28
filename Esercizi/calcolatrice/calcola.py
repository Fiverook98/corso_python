 #Richiesta input
a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))
op = input("""Inserisci l'operazione che vuoi effettuare 
(+) Addizione 
(-) Sottrazione
(*) Moltiplicazione 
(/) Divisione 
>>>> """)

#Dichiarazione variabili
cons = True
op_cons = ['+','-','*','/']
risult = "Operazione fallita! Riprova!"

#Controllo operazione
if op == op_cons[0]:
    risult = a + b
elif op == op_cons[1]:
    risult = a - b
elif op == op_cons[2]:
    risult = a * b
elif op == op_cons[3]:
    #Controllo errore divisione per 0
    if b == 0:
        risult = "Errore! Divisione per zero non consentita!"
        cons = False
    else:
        risult = a / b   
else:
    risult = "Il carattere inserito non fa parte delle operazioni valide!"
    cons = False

#Comunicazione risultato

if cons:
    print(f"Il risultato dell'operazione {a} {op} {b} = {risult:.2f}")
else:
    print(risult)

