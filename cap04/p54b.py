def fib(n):
    """Fibonacci:
    fib(n) = fib(n - 1) + fib(n - 2) se n > 1
    fib(n) = 1 se n <= 1
    """
    # Dois primeiros valores
    l = [1, 1]

    # Calculando os outros
    for i in range(2, n + 1):
        l.append(l[i -1] + l[i - 2])
    return l[n]

# Mostrar os primeiros elementos de Fibonacci
for i in range(6):
    print(i, '=>', fib(i))
