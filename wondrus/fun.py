from typing import Generator
def wondrous(n):
    """Restituisci una lista di numeri HOTPO, a partire da n."""
    mylist = []
    while n != 1:
        mylist.append(n)
        n = n // 2 if n % 2 == 0 else 3*n + 1 
    mylist.append(1)
    return mylist

def wondrous_gen(n: int) -> Generator[int, None, None]:
    """Restituisci una lista di numeri HOTPO, a partire da n."""
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0  else 3*n + 1
    yield 1