a = float(input("Digitare il primo numero: "))
b = float(input("Digitare il secondo numero: "))

m = a if a < b else b
print(f"Il numero più grande tra {a} e {b} è {m}")