import os.path
import glob

# Mostra uma lista de nomes de arquivos
# e seus respectivos tamanhos
for arq in sorted(glob.glob('*.py')):
    print(arq, os.path.getsize(arq))
