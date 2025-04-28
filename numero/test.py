a = float(input("Inserire l'estremo sinistra dell'intervallo: "))
b = float(input("Inserire l'estremo destro dell'intervallo: "))
x = float(input(f"Digitare valore di cui verificare l'appartenenza nell'intervallo [{a},{b}]"))

if x >= a:
    if x <= b:
        appartiene = True
    else:
        appartiene = False
else:
    appartiene = False

if appartiene:
    s = ''
else:
    s = 'non'

MSG_fin = f"Il numero {x}{s} appartiene all'intervallo [{a},{b}]"
print(MSG_fin)