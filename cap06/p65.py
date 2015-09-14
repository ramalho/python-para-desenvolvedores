def calc():

    def ad1(temp):
        temp += 1
        return temp

    def ad2():
        nonlocal temp
        temp += 2
        return temp

    temp = 0
    # Soma 1 a temp
    temp = ad1(temp)
    # Soma 2 a temp
    ad2()
    return temp

temp = 5  # Variável global
print(calc())  # Retorna 3
