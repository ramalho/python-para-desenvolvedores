# Função com anotações

def eq2g(a: int, b: int, c: int):
    """Retorna raízes para equações de 2º grau"""
    if a == 0: # Uma reta
        return -c / b,
    else:
        d = (b**2 - 4*a*c) ** 0.5
        x1 = (-b - d) / (2 * a)
        x2 = (-b + d) / (2 * a)
        return x1, x2

# Alguns testes
print(eq2g(0, 2, -2))
print(eq2g(1, -2, 0))
print(eq2g(2, 2, 0))
print(eq2g(2, 0, 2))

# Mostra a ajuda
help(eq2g)

# Anotações
print(eq2g.__annotations__)
