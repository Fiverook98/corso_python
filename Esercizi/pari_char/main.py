str_in = input("Inserisci la tua parola: ")
lun = len(str_in)

for i in range(0, lun, 2):
    print(str_in[i])
