"""
Lendo um arquivo compactado
"""
import zipfile

# Abre o arquivo zip para leitura
zip = zipfile.ZipFile('arq.zip')

# Pega a lista dos arquivos compactados
arqs = zip.namelist()
for arq in arqs:
    # Mostra o nome do arquivo
    print('Arquivo:', arq)
    # Pegando as informações do arquivo
    zipinfo = zip.getinfo(arq)
    print('Tamanho original:', zipinfo.file_size)
    print('Tamanho comprimido:', zipinfo.compress_size)
    # Mostra o conteúdo do arquivo
    print(zip.read(arq).decode('utf8'))
