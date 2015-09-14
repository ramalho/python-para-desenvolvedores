import time

# localtime() Retorna a data e hora local no formato
# de uma estrutura chamada struct_time, que é uma
# coleção com os itens: ano, mês, dia, hora, minuto,
# segundo, dia da semana, dia do ano e horário de verão
print(time.localtime())

# asctime() retorna a data e hora como string, conforme
# a configuração do sistema operacional
print(time.asctime())

# time() retorna o tempo do sistema em segundos
ts1 = time.time()

# gmtime() converte segundos para struct_time
tt1 = time.gmtime(ts1)
print(ts1, '->', tt1)

# Somando uma hora
tt2 = time.gmtime(ts1 + 3600.)

# mktime() converte struct_time para segundos
ts2 = time.mktime(tt2)
print(ts2, '->', tt2)

# clock() retorma o tempo desde quando o programa
# iniciou, em segundos
print('O programa levou', time.clock(),
    'segundos até agora...')

# Contando os segundos...
for i in range(5):
    # sleep() espera durante o número de segundos
    # especificados como parâmetro
    time.sleep(1)
    print(i + 1, 'segundo(s)')
