# String unicode
u = 'Hüsker Dü'

# Convertendo para bytes
s = u.encode('latin1')
print(s, '=>', type(s))

# Bytes para unicode
s = bytes('Hüsker Dü', 'latin1')
u = s.decode('latin1')
print(u, '=>', type(u))
