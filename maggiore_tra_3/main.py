a = int(input("Inserisci il primo numero  : "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo numero  : "))

if a == b and b == c:
    Risul = "I numeri sono identici"
else:
    Risul = f"Il più grande tra {a}, {b} e {c} è {(a if a>=c else c) if a >= b else (c if c>=b else c)}"

print(Risul)