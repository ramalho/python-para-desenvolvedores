import string
# Cria uma string template
st = string.Template('$aviso aconteceu em $quando')

# Preenche o modelo com um dicionário
s = st.substitute({'aviso': 'Falta de eletricidade',
    'quando': '03 de Abril de 2002'})

# Mostra:
# Falta de eletricidade aconteceu em 03 de Abril de 2002
print(s)
