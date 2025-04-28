lista = eval(input("Inserire una lista: "))
iteratore = iter(lista)
massimo = next(iteratore)
len_massimo = len(massimo)

for el in iteratore:
    if len(el) > len_massimo:
        massimo = el
        len_massimo = len(el)

print(massimo, len_massimo)