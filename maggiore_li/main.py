a = int(input("Inserisci quanto sarà grande la tua lista: "))
li = []
for i in range(a):
    i = int(input("Scrivi il numero che vuoi inserire nella lista: "))
    li.append(i)
print(f"Questa è la tua lista: {li}")
j = li[0]
for i in range(len(li)):
    if j < li[i]:
        j = li[i]

print(f"Il numero più grande della tua lista è {j}")
