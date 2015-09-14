dados = [(4, 3), (5, 1), (7, 2), (9, 0)]

# Comparando pelo último elemento
def _key(x):
    return x[-1]

print('Lista:', dados)

# Ordena usando _key()
print('Ordenada:', sorted(dados, key=_key))
