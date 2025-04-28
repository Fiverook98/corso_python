#Funzione somma
def somma(a,b):
    return a + b

#Funzione sottrazione
def sottr(a,b):
    return a - b

#Funzione moltiplicazione
def prodotto(a,b):
    return a * b

#Funzione di divisione con controllo
def divisione(a,b):
    return (a // b if a % b == 0 else a / b) if b != 0 else "Divisione per 0 non consentita"

#Funzione di modulo
def modulo(a,b):
    return a % b

