from operazioni import *

#Funzione di richiesta
def richiesta():
    a = float(input("Inserisci il primo numero        : "))
    b = float(input("Inserisci il secondo numero      : "))
    op = input("Inserisci l'operazione da effettuare: ")
    return a,b,op

#Funzione calcolatrice
def calcolatrice(a,b,op):
    operazioni_consentite = {'+' : somma, '-': sottr, '*': prodotto, '/': divisione, '%':modulo }
    if op in operazioni_consentite:
        return f"Il risultato è [{a} {op} {b} = {operazioni_consentite[op](a,b)}]"
    else:
        return "Operazione fallita! Riprova!"