from fun import wondrous, wondrous_gen

n = int(input("Inserisci un numero intero positivo: "))
for i in wondrous(n):
    print(i, end = ' ')
    if n // i == 2:
        break

g = wondrous_gen(n)

print()

for i in g:
    print(i, end = ' ')
    if n // i == 2:
        break

print(g.__next__())