import sys
from subprocess import Popen, PIPE

# ping
cmd = 'ping -c 1 '

# No Windows
if sys.platform == 'win32':
    cmd = 'ping -n 1 '

# Local só para testar
host = '127.0.0.1'

# Comunicação com outro processo,
# um pipe com o stdout do comando
py = Popen(cmd + host, stdout=PIPE)

# Mostra a saída do comando
print(py.stdout.read())
