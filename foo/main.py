def foo():
    print("Inizia l'esecuzione del codice...")
    x = True
    while x != 'python':
        x = (yield)
        print(x)
    print("Termina l'esecuzione del codice...")

g = foo()
for el in g:
    g.send(input("Inserire il valore da inviare: "))
    print(el)