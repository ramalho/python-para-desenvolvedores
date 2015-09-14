"""
Gravando texto em um arquivo compactado
"""

import zipfile

texto = """
***************************************
Esse é o texto que será compactado e...
... guardado dentro de um arquivo zip.
***************************************
"""

# Cria um zip novo
zip = zipfile.ZipFile('arq.zip', 'w',
    zipfile.ZIP_DEFLATED)

# Escreve uma string no zip como se fosse um arquivo
zip.writestr('texto.txt', texto.encode('utf8'))

# Fecha o zip
zip.close()
