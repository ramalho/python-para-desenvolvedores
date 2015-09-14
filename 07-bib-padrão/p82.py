import re

# Compilando a expressão regular
# Usando compile() a expressão regular fica compilada
# e pode ser usada mais de uma vez
rex = re.compile('\w+')

# Encontra todas as ocorrências que atendam a expressão
bandas = 'Yes, Genesis & Camel'
print(bandas, '->', rex.findall(bandas))

# Identifica as ocorrências de Björk (e suas variações)
bjork = re.compile('[Bb]j[öo]rk')
for m in ('Björk', 'björk', 'Biork', 'Bjork', 'bjork'):
    # match() localiza ocorrências no início da string
    # para localizar em qualquer parte da string, use search()
    print(m, '->', bool(bjork.match(m)))

# Substituindo texto
texto = 'A próxima faixa é Stairway to Heaven'
print(texto, '->', re. sub('[Ss]tairway [Tt]o [Hh]eaven',
    'The Rover', texto))

# Dividindo texto
bandas = 'Tool, Porcupine Tree e NIN'
print(bandas, '->', re.split(',?\s+e?\s+', bandas))
