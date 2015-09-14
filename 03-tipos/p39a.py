s = bytearray(b'Python')
s[0] = ord('p') # ord() retorna o valor ASCII do caracter
print(s.decode()) # mostra "python"
