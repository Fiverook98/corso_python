a = int(input("Inserisci il numero per l'iterazione: "))
previus_num = 0
for n in range(a):
    som = previus_num + n
    print(f"Numero attuale {n}, Numero precedente {previus_num}, Somma: {som}")
    previus_num = n

    
    