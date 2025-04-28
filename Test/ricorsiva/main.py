def ric_list(li):
    if len(li) == 1:
        return li[0]
    else:
        return li[0] + ric_list(li[1::])
    
li = eval(input("Inserisci la tua lista: "))

print(ric_list(li))