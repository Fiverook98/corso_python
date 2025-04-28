#Richiesta voti
voto1 = float(input("Inserire voto prima verifica  : "))
voto2 = float(input("Inserire voto seconda verifica: "))
voto3 = float(input("Inserire voto terza verifica  : "))
media = (voto1 + voto2 + voto3) / 3

#Comunicazione media
print(f"Media = {media:.1f}", end = ' ')

#Controllo dei giudizi
if media < 4.5:
    giudizio = "Gravemente Insufficiente"
elif media < 6.0:
    giudizio = "Insufficiente"
elif media < 7.5:
    giudizio = "Sufficiente"
else:
    giudizio = "Buono"

#Comunicazione giudizio ottenuto
print(f"Giudizio = {giudizio}")