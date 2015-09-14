import csv

# Dados
dt = (('temperatura', 15.0, 'C', '10:40', '2006-12-31'),
    ('peso', 42.5, 'kg', '10:45', '2006-12-31'))

# A rotina de escrita recebe um objeto do tipo file
out = csv.writer(open('dt.csv', 'w', newline=''))

# Escrevendo as tuplas no arquivo
out.writerows(dt)
