import csv

# A rotina de leitura recebe um objeto arquivo
dt = csv.reader(open('dt.csv'))

# Para cada registro do arquivo, imprima
for reg in dt:
    print(reg)
