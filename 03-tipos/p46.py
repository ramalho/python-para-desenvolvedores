dic = {'nome': 'Shirley Manson', 'banda': 'Garbage'}

# Acessando elementos:
print('Nome:', dic['nome'])

# Adicionando elementos:
dic['album'] = 'Version 2.0'

# Apagando um elemento do dicionário:
del dic['album']

# Obtendo os itens, chaves e valores:
print('itens:', dic.items())
print('chaves:', dic.keys())
print('valores:', dic.values())
