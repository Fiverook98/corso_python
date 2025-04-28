def fibonacci(n: int) -> list:
    if n == 1:
        return 0
    if n == 2:
        return [0, 1]
    fibo_list = [0, 1]
    xk, xkm1 = fibo_list[-1::]
    for i in range(3,n + 1):
        xkm1, xk = xk, xk + xkm1
        fibo_list.append(xk)
    return fibo_list