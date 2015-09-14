def somalista(lista):
    """Soma listas de listas, recursivamente
    Coloca o resultado como global"""
    global soma
    for item in lista:
        if type(item) is list:  # Se o tipo do item for lista
            somalista(item)
        else:
            soma += item

soma = 0
somalista([[1, 2], [3, 4, 5], 6])
print(soma)  # 21
