# Fatorial implementado de forma recursiva
def fatorial(num):
    if num <= 1:
        return 1
    else:
        return(num * fatorial(num - 1))

# Testando fatorial()
print(fatorial(5))
