import tempfile

# cria um arquivo temporário
temp = tempfile.TemporaryFile()

# Escreve no arquivo temporário
temp.write(b'Teste')

# Volta para o início do arquivo
temp.seek(0)

# Mostra o conteúdo do arquivo
print(str(temp.read(), encoding='utf8'))

# Fecha o arquivo
temp.close()
