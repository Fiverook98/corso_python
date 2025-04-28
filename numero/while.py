start = int(input("Inserire l'estremo sinistro: "))
stop = int(input("Inserire l'estremo destro: "))
step = int(input("Inserire il passo di campionamento: "))
elem_inter = int(input("Inserire il valore di interruzione: "))

i = start

while i <= stop:
    if i == elem_inter:
        print(f"Generato elem_inter: {i=}")
        print("Ciclo terminato a causa di un'interruzione Break")
        break
    print(f"Generato numero: {i}")
    i += step
else:
    print("Il ciclo While è terminato normalmente")

print("Sono fuori dal ciclo While")