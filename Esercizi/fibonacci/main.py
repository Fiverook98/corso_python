def fibonacci(n: int):
   a, b = 0, 1
   for i in range(n):
      yield a
      a, b = b, a+b

n = int(input("Inserisci il numero di elementi che vuoi siano restituiti>>> "))
g = fibonacci(n)

for i in g:
   print(i, end =' | ')
   
