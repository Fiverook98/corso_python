a = float(input("Inserire il primo numero: "))
b = float(input("Inserire il secondo numero: "))
c = float(input("Inserire il terzo numero: "))

m = (a if a < c else c) if a < b else (b if b < c else c)
print(f"Il minimo tra {a},{b},{c} è {m}")