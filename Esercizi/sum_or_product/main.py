#Richiest degli elementi
a = int(input("Inserisci il primo numero  : "))
b = int(input("Inserisci il secondo numero: "))

def choose(a,b):
    product_limit = 1000
    if (a * b) >= product_limit:
        print("I valori superano il Product Limit. Verrà effettuata la somma!")
        return a + b
    else:
        return a * b
    


